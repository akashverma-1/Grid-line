import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pandas as pd
import os



def automate_cleaning(datasets, task_id = [1,2,3,4], nrows=10000):
    print('cleaning tasks', task_id)
    if task_id == []:
        task_id = [1,2,3,4]
    os.makedirs('static/cleaned_data', exist_ok=True)
    tasks = {
        1: 'impute',
        2: 'normalize',
        3: 'drop duplicates',
        4: 'encode'
    }
    print('available cleaning tasks', tasks)
    print(f'datasets to clean: {datasets}')
    clean_files = []
    for i, dataset in enumerate(datasets):
        print(f"Cleaning dataset {i+1}/{len(datasets)}")
        try:
            df = pd.read_csv(dataset, nrows=nrows)
        # encoding error
        except UnicodeDecodeError:
            df = pd.read_csv(dataset, encoding='latin1', nrows=nrows)
        except:
            print(f"Error reading {dataset}")
            continue
        
        if 4 in task_id:
            df = df.drop_duplicates()
        print(f'columns before cleaning: {df.columns}')
        num_cols = df.select_dtypes(include='number').columns
        cat_cols = df.select_dtypes(exclude='number').columns

        if 1 in task_id and 2 in task_id and 3 in task_id:
            preprocessor = ColumnTransformer(
                transformers=[
                    ('num', Pipeline(steps=[
                        ('imputer', SimpleImputer(strategy='mean')),
                        ('scaler', StandardScaler())
                    ]), num_cols),
                    ('cat', Pipeline(steps=[
                        ('imputer', SimpleImputer(strategy='most_frequent')),
                        ('encoder', OrdinalEncoder())
                    ]), cat_cols)
                ])
            
            df_cleaned = preprocessor.fit_transform(df)
            df_cleaned = pd.DataFrame(df_cleaned, columns=num_cols.append(cat_cols))
            df_cleaned.to_csv(f'static/cleaned_data/{os.path.basename(dataset)}', index=False)
        
        elif 1 in task_id and 2 in task_id:
            preprocessor = ColumnTransformer(
                transformers=[
                    ('num', Pipeline(steps=[
                        ('imputer', SimpleImputer(strategy='mean')),
                        ('scaler', StandardScaler())
                    ]), num_cols),
                    ('cat', Pipeline(steps=[
                        ('imputer', SimpleImputer(strategy='most_frequent'))
                    ]), cat_cols)
                ])
            
            df_cleaned = preprocessor.fit_transform(df)
            df_cleaned = pd.DataFrame(df_cleaned, columns=num_cols.append(cat_cols))
            df_cleaned.to_csv(f'static/cleaned_data/{os.path.basename(dataset)}', index=False)

        elif 1 in task_id and 3 in task_id:
            preprocessor = ColumnTransformer(
                transformers=[
                    ('num', Pipeline(steps=[
                        ('imputer', SimpleImputer(strategy='mean'))
                    ]), num_cols),
                    ('cat', Pipeline(steps=[
                        ('imputer', SimpleImputer(strategy='most_frequent')),
                        ('encoder', OrdinalEncoder())
                    ]), cat_cols)
                ])
            
            df_cleaned = preprocessor.fit_transform(df)
            df_cleaned = pd.DataFrame(df_cleaned, columns=num_cols.append(cat_cols))
            df_cleaned.to_csv(f'static/cleaned_data/{os.path.basename(dataset)}', index=False)

        elif 2 in task_id and 3 in task_id:
            preprocessor = ColumnTransformer(
                transformers=[
                    ('num', Pipeline(steps=[
                        ('scaler', StandardScaler())
                    ]), num_cols),
                    ('cat', Pipeline(steps=[
                        ('encoder', OrdinalEncoder())
                    ]), cat_cols)
                ])
            
            df_cleaned = preprocessor.fit_transform(df)
            df_cleaned = pd.DataFrame(df_cleaned, columns=num_cols.append(cat_cols))
            df_cleaned.to_csv(f'static/cleaned_data/{os.path.basename(dataset)}', index=False)
        
        elif 1 in task_id:
            preprocessor = ColumnTransformer(
                transformers=[
                    ('num', Pipeline(steps=[
                        ('imputer', SimpleImputer(strategy='mean'))
                    ]), num_cols),
                    ('cat', Pipeline(steps=[
                        ('imputer', SimpleImputer(strategy='most_frequent'))
                    ]), cat_cols)
                ])
            
            df_cleaned = preprocessor.fit_transform(df)
            df_cleaned = pd.DataFrame(df_cleaned, columns=num_cols.append(cat_cols))
            df_cleaned.to_csv(f'static/cleaned_data/{os.path.basename(dataset)}', index=False)
        
        elif 2 in task_id:
            preprocessor = ColumnTransformer(
                transformers=[
                    ('num', Pipeline(steps=[
                        ('scaler', StandardScaler())
                    ]), num_cols),
                    ('cat', Pipeline(steps=[
                        ('imputer', SimpleImputer(strategy='most_frequent'))
                    ]), cat_cols)
                ])
            
            df_cleaned = preprocessor.fit_transform(df)
            df_cleaned = pd.DataFrame(df_cleaned, columns=num_cols.append(cat_cols))
            df_cleaned.to_csv(f'static/cleaned_data/{os.path.basename(dataset)}', index=False)

        elif 3 in task_id:
            preprocessor = ColumnTransformer(
                transformers=[
                    ('num', Pipeline(steps=[
                        ('imputer', SimpleImputer(strategy='mean'))
                    ]), num_cols),
                    ('cat', Pipeline(steps=[
                        ('encoder', OrdinalEncoder())
                    ]), cat_cols)
                ])
            
            df_cleaned = preprocessor.fit_transform(df)
            df_cleaned = pd.DataFrame(df_cleaned, columns=num_cols.append(cat_cols))
            df_cleaned.to_csv(f'static/cleaned_data/{os.path.basename(dataset)}', index=False)

        else:
            print("No task was selected")
            continue

        clean_files.append(f'static/cleaned_data/{os.path.basename(dataset)}')
        print(f"Dataset cleaned and saved as static/cleaned_data/{os.path.basename(dataset)}")
    return clean_files





if __name__ == '__main__':
    automate_cleaning(['static/uploads/Dry_Bean_Dataset.csv'])