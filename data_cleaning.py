def clean_data(df):
    df = df.drop_duplicates()

    # Xử lý NaN
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
    df['Cabin'] = df['Cabin'].fillna("Unknown")

    # Chuẩn hóa cho máy (ẩn)
    df['_Sex_Code'] = df['Sex'].map({'male': 0, 'female': 1})
    df['_Embarked_Code'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

    return df