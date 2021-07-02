import pandas as pd
import numpy as np

directory = r"C:\Users\Amaury\Documents\Data_Science_BECODE\Projects\Python\GNT-Arai-2.31\content\4.machine_learning\0.data_preprocessing\Nycity-trees\2015_Street_Tree_Census_-_Tree_Data.csv"
df_data_100000_ori = pd.read_csv(directory, sep=',').iloc[0:100,:]
df_data_100000 = df_data_100000_ori.copy()
#print(df_data_100000)
#print(df_data_100000.columns)
# print(df_data_100000.shape)
# print(df_data_100000.shape())
# print(df_data_100000.info)
print(df_data_100000.dtypes)
#df_data_100000.head()

def remove_empty_rows(self, df):
    return df.dropna(how='all')


def drop_duplicates(column):
    df_data_100000.drop_duplicates(subset=column, keep=False)


def fill_undefined(column):
    df_data_100000[column] = df_data_100000[column].fillna(value='undefined')


def fill_zeros(column):
    df_data_100000[column] = df_data_100000[column].fillna(value='0')


def change_to_date_type(column):
    df_data_100000[column] = df_data_100000[column].astype("datetime64[ns]")


def change_to_bool(column):
    df_data_100000[column] = df_data_100000[column].astype("bool")


def change_to_int(column):
    df_data_100000[column] = df_data_100000[column].astype("int64")


def change_to_obj(column):
    df_data_100000[column] = df_data_100000[column].astype("str")


def change_no_yes_to_false_true(columns_list):
    for column in columns_list:
        df_data_100000[column] = df_data_100000[column].replace(to_replace="No", value=False)
        df_data_100000[column] = df_data_100000[column].replace(to_replace="Yes", value=True)

def change_to_category(column):
    df_data_100000[column] = df_data_100000[column].astype("str")
# print(df_data_100000)
# print(df_data_100000.isnull().any())
# print(df_data_100000.isna().sum())

# columns_to_float =
# columns to

# def drop_duplicates(column, replace_nan_value):
#     self.df[column] = self.df[column].fillna(replace_nan_value)
#
# def apply_fillna_to_column(self, column, replace_nan_value):
#     self.df[column] = self.df[column].fillna(replace_nan_value)
#
# def count_nans_in_df(self):
#     return self.df.isna().sum()


# first drop duplicates in the tree_id column

df_data_100000 = df_data_100000.drop(["state", "borocode", "nta", "problems"], axis = 1)

drop_duplicates("tree_id")

# add undefined in the object columns
columns_to_be_undefined = ["sidewalk", "guards", "steward", "health", "spc_latin", "spc_common"]
fill_undefined(columns_to_be_undefined)

# fill in with zeros in the int columns
columns_for_zero = ["council district", "census tract", "bin", "bbl"]
fill_zeros(columns_for_zero)

# change yes/no into True/False
booleanize_these_columns = ["root_stone", "root_grate", "root_other", "trunk_wire", "trnk_light", "trnk_other", "brch_light", "brch_shoe", "brch_other"]
change_no_yes_to_false_true(booleanize_these_columns)

# make booleans out of the yes/no
change_to_bool(booleanize_these_columns)

# change into date data type
cols_to_date_type = ["created_at"]
change_to_date_type(cols_to_date_type)


# change into string data type
columns_to_string = ["boro_ct"]
change_to_obj(columns_to_string)

# change into int data type
columns_to_int = ["council district", "census tract", "bin", "bbl"]
change_to_int(columns_to_int)

# check types
print(df_data_100000.dtypes)

columns_to_be_lowercased = ["curb_loc", "status", "health", "spc_latin", "spc_common", "nta_name", "steward", "guards", "sidewalk", "user_type", "address", "zip_city", "borough"]
#lowercase(columns_to_be_lowercased)

df_data_100000[columns_to_be_lowercased] = df_data_100000[columns_to_be_lowercased].apply(lambda value: value.astype(str).str.lower())

# checks missing data:
print("----- columns with missing values = True -------->")
print(df_data_100000.isnull().any())
print("----------- missing values check END ------------>")

# check types
# print(df_data_100000.dtypes)

# make clean csv file
def write_to_csv(file_path):
    df_data_100000.to_csv(file_path)

write_to_csv("clean_trees.csv")
