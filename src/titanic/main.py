import logging
import sys

import pandas as pd

from titanic import Storage, arguments, credentials, models, transformations


def main(config: arguments.Config):
    credentials.load()
    logging.info("Credentials loaded")

    storage = Storage(config.bucket)

    classifier, accuracy = train_classifier(storage, dataset=config.train_path)
    logging.info(f"Trained classifier with {accuracy} accuracy")

    predictions = predict_survival(
        storage, dataset=config.test_path, classifier=classifier
    )
    logging.info(f"Made {len(predictions)} predictions")

    storage.write_csv(predictions, config.output_path)
    logging.info("Done writing results")


def train_classifier(storage: Storage, dataset: str):
    df_train = storage.read_csv(path=dataset)
    df_train = transformations.add_all_features(df_train)

    train_features = transformations.select_features_for_ml(df_train)
    train_target = transformations.select_target_for_ml(df_train)

    classifier = models.fit_random_forest(train_features, train_target)
    return classifier


def predict_survival(storage: Storage, dataset: str, classifier) -> pd.DataFrame:
    df_test = storage.read_csv(path=dataset)
    df_test = transformations.add_all_features(df_test)

    test_data = transformations.select_features_for_ml(df_test)
    df_test["Survived"] = classifier.predict(test_data)

    return df_test[["PassengerId", "Survived"]]


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    main(arguments.parse())
