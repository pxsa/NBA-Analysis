import pandas as pd
import matplotlib.pyplot as plt


class EDA:

    def __init__(self, df):
        self.df = df


    def shape(self):
        return self.df.shape


    def info(self):
        return self.df.info()


    def missing_values(self):
        return self.df.isnull().sum()


    def statistics(self):
        return self.df.describe()


    def duplicates(self):
        return self.df.duplicated().sum()


    def numerical_summary(self):
        return self.df.describe()


    def categorical_summary(self):

        categorical_cols = [
            "team_code",
            "shoots"
        ]

        result = {}

        for col in categorical_cols:
            result[col] = self.df[col].value_counts()

        return result


    def correlation(self):

        numeric_df = self.df.select_dtypes(
            include="number"
        )

        return numeric_df.corr()


    def plot_correlation(self, save_path=None):

        corr = self.correlation()

        plt.figure(figsize=(10,8))

        plt.imshow(corr)

        plt.colorbar()

        plt.xticks(
            range(len(corr.columns)),
            corr.columns,
            rotation=90
        )

        plt.yticks(
            range(len(corr.columns)),
            corr.columns
        )

        plt.title("Correlation Matrix")


        if save_path:
            plt.savefig(
                save_path,
                bbox_inches="tight"
            )

        plt.show()


    def plot_distribution(self, column, save_path=None):

        plt.figure(figsize=(8,5))

        plt.hist(
            self.df[column],
            bins=30
        )

        plt.xlabel(column)
        plt.ylabel("Frequency")

        plt.title(
            f"Distribution of {column}"
        )


        if save_path:
            plt.savefig(
                save_path,
                bbox_inches="tight"
            )

        plt.show()



    def top_players(self, metric, n=10):

        result = (
            self.df
            .groupby("full_name")[metric]
            .mean()
            .sort_values(ascending=False)
            .head(n)
        )

        return result



    def team_analysis(self):

        clean_df = self.df[
            ~self.df["team_code"].isin(
                ["2TM", "3TM", "4TM"]
            )
        ]

        result = (
            clean_df
            .groupby("team_code")["win_shares"]
            .sum()
            .sort_values(
                ascending=False
            )
        )

        return result
    
    def data_types(self):

        return self.df.dtypes
    
    
    def outlier_summary(self):

        numeric_df = self.df.select_dtypes(
            include="number"
        )

        result = {}

        for col in numeric_df.columns:

            Q1 = numeric_df[col].quantile(0.25)
            Q3 = numeric_df[col].quantile(0.75)

            IQR = Q3 - Q1

            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR

            outliers = numeric_df[
                (numeric_df[col] < lower) |
                (numeric_df[col] > upper)
            ]

            result[col] = len(outliers)

        return result