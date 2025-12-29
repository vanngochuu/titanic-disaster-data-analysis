import matplotlib.pyplot as plt


def plot_survival(df):
    data = df['Survived'].map({0: 'Chết', 1: 'Sống'}).value_counts()
    data.plot(kind='bar')
    plt.title("Tỉ lệ sống sót của hành khách")
    plt.xlabel("Tình trạng")
    plt.ylabel("Số lượng")
    plt.xticks(rotation=0)
    plt.show()


def plot_gender(df):
    data = df.groupby('Sex')['Survived'].mean() * 100
    data.index = data.index.map({'male': 'Nam', 'female': 'Nữ'})
    data.plot(kind='bar')
    plt.title("Tỉ lệ sống sót theo giới tính (%)")
    plt.xlabel("Giới tính")
    plt.ylabel("Phần trăm sống sót")
    plt.xticks(rotation=0)
    plt.show()