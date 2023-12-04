import pandas as pd

from titanic import transformations


def test_add_sex_feature():
    df = pd.DataFrame({"Sex": ["male", "male", "female", "male", "female"]})
    df = transformations.add_sex_feature(df)

    assert len(df[df["Sex_F"] == 1]) == 3
    assert len(df[df["Sex_F"] == 0]) == 2


def test_add_age_feature():
    df = pd.DataFrame(
        {
            "Sex": [
                "male",
                "male",
                "female",
                "male",
                "female",
                "female",
                "female",
                "male",
                "female",
                "female",
                "male",
                "male",
            ],
            "Age": [
                12,
                38,
                27,
                None,
                15,
                None,
                None,
                17,
                27,
                2,
                None,
                17,
            ],
            "Class": [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2],
        }
    )

    transformations.add_age_feature(df)

    assert df["Age_F"][3] == 25
    assert df["Age_F"][5] == 21
    assert df["Age_F"][6] == 14.5
    assert df["Age_F"][10] == 17
