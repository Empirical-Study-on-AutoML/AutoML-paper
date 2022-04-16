# -*- coding: utf-8 -*-
"""Dec 5_data cleaning in order to get the unique name of the repositories.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pi0NAdjW_2lOZINnMwo_Xq73D2VYVExU
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
df1=pd.read_csv('/content/drive/MyDrive/PhD/Automate machine learning/presentations for the meetings/12th meeting/input_data/Dec1_splited_name_of_the_repositories_part_1.csv')
df2=pd.read_csv('/content/drive/MyDrive/PhD/Automate machine learning/presentations for the meetings/12th meeting/input_data/Dec1_splited_name_of_the_repositories_part_2.csv')
df3=pd.read_csv('/content/drive/MyDrive/PhD/Automate machine learning/presentations for the meetings/12th meeting/input_data/Dec1_splited_name_of_the_repositories_part_11.csv')
df4=pd.read_csv('/content/drive/MyDrive/PhD/Automate machine learning/presentations for the meetings/12th meeting/input_data/Dec1_splited_name_of_the_repositories_part_22.csv')

df=pd.concat([df1, df2,df3,df4], ignore_index=True)

df

df.drop_duplicates(subset ="repo_name",keep = "first", inplace = True)

df

df=df[df["repo_name"].str.contains("assignment")==False]
df=df[df["repo_name"].str.contains("Assignment")==False]
df=df[df["repo_name"].str.contains("book")==False]
df=df[df["repo_name"].str.contains("Book")==False]
df=df[df["repo_name"].str.contains("chapter")==False]
df=df[df["repo_name"].str.contains("Chapter")==False]
df=df[df["repo_name"].str.contains("tutorial")==False]
df=df[df["repo_name"].str.contains("Tutorial")==False]
df=df[df["repo_name"].str.contains("course")==False]
df=df[df["repo_name"].str.contains("Course")==False]

df

output_path="/content/drive/MyDrive/PhD/Automate machine learning/presentations for the meetings/12th meeting/input_data/"
df.to_csv(output_path+"Dec5_merged_name_of_the_repositories.csv")