import pandas as pd
import numpy as np

def validate_address(input_file, abp_file, output_file):

    """
    A function to read in input and abp csv files and output a csv file that contains the original input data and
    an extra Street_In_Postcode column that flags addresses that have street names that are consistent
    / inconsistent with their postcode based on data in abp file.

    NB. Street_In_Postcode will be False if Postcode not present in abp file. This can be easily altered to be
    'Unknown' if desired.
    """

    # Load input data and combine address into single column.
    input_df = pd.read_csv(input_file, encoding='utf-8', dtype=str).fillna('')
    input_df['Address'] = input_df[[f'Address_Line_{i}' for i in range(1, 6)]].astype(str).agg(' '.join, axis=1)

    # Load relevant abp data.
    abp_df = pd.read_csv(abp_data, encoding='utf-8').rename(columns={'POSTCODE':'Postcode'})[['Postcode', 'STREET_NAME']].fillna('')

    # Merge data frames on postcode and set 'Street_In_Postcode' True where street name in address. Vectorize for
    # efficiency.
    merged_df = input_df.merge(abp_df, how='left', on='Postcode')
    print(len(merged_df))
    merged_df['Street_In_Postcode'] = np.vectorize(lambda street, address: street.lower() in address.lower() and street != '')(merged_df['STREET_NAME'].astype(str), merged_df['Address'])
    print(len(merged_df))
    # Output csv.
    merged_df.drop(['Address'], axis=True, inplace=True)
    merged_df.to_csv('example_output_data.csv', index=False, encoding='utf-8')



if __name__ == "__main__":
    input_data = 'example_input_data.csv'
    abp_data = 'example_abp_data.csv'
    output_data = 'example_output_data.csv'
    validate_address(input_data, abp_data, output_data)
