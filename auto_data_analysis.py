import pandas as pd
from ydata_profiling import ProfileReport
import os
def automate_analysis(filepath):
    df = pd.read_csv(filepath)
    profile = ProfileReport(df, explorative=True, 
                            minimal=True,
                            dark_mode=True, 
                            title=f'{filepath.split("/")[-1].split(".")[0]} Summary',
                            html = {
                                'navbar_show':False
                            })
    os.makedirs('static/reports', exist_ok=True)
    save_path = f'static/reports/{filepath.split("/")[-1].split(".")[0]}_report.html'
    profile.to_file(save_path)
    return save_path


def launch_data_analysis(file_paths):
    results = []
    for file in file_paths:
        results.append({
            'file': file,
            'report': automate_analysis(file)
        })
    return results


if __name__ == '__main__':
    print(launch_data_analysis([r'static\uploads\links.csv']))





