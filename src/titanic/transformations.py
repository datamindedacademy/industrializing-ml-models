import numpy as np
import pandas as pd


def add_age_feature(data: pd.DataFrame) -> pd.DataFrame:
    data["Age_F"] = data["Age"]
    data["Age_F"] = (
        data["Age_F"]
        .groupby([data["Sex"], data["Class"]], group_keys=False)
        .apply(lambda x: x.fillna(x.median()))
    )
    return data


def add_sex_feature(data: pd.DataFrame) -> pd.DataFrame:
    sexes = sorted(data["Sex"].unique())
    genders_mapping = dict(zip(sexes, range(0, len(sexes) + 1)))
    data["Sex_F"] = data["Sex"].map(genders_mapping).astype(int)
    return data


def add_embarked_feature(data: pd.DataFrame) -> pd.DataFrame:
    data["Embarked_F"] = data["Embarked"].fillna("S")
    data["Embarked_F"] = data["Embarked_F"].map({"S": 0, "C": 1, "Q": 2})
    return data


def add_family_size_feature(data: pd.DataFrame) -> pd.DataFrame:
    data["FamilySize_F"] = data["Siblings"] + data["ParentsChildren"]
    return data


def add_all_features(data: pd.DataFrame) -> pd.DataFrame:
    # Defensive copy to avoid modifying source dataframe
    return (
        data.copy()
        .pipe(add_age_feature)
        .pipe(add_sex_feature)
        .pipe(add_embarked_feature)
        .pipe(add_family_size_feature)
    )


def select_features_for_ml(data: pd.DataFrame, include_id: bool = False) -> np.ndarray:
    columns = ["Class", "Age_F", "Sex_F", "Embarked_F", "FamilySize_F"]
    if include_id:
        columns = ["PassengerId", *columns]

    return data[columns].values


def select_target_for_ml(data: pd.DataFrame) -> np.ndarray:
    return data["Survived"].values
