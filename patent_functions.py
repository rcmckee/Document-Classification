


def pd_col_to_category(data_frame, list_o_columns):
    '''
    input:
    data_frame - a pandas dataframe
    list_o_columns - list of columns you want converted to data type category
    
    output: None, it changes the column in the data frame to a data type category
    '''
    for col in list_o_columns:
        data_frame[col] = data_frame[col].astype('category')

def print_artUnit_uspcClass(art_unit_list, uspc_class):
    '''
    input:
    art_unit_list - a list of art units in the art_unit column
    uspc_class - a 'string' single uspc class that appears in the uspc_class column. Typically the class that covers the art units you entered in a list.
    
    output:
    prints the art unit or uspc class and the number of times it appears.

    exampl:

=======
    art_unit_list_3600 = [3622,3623,3623,3625,3625,3626,3627,3627,3627,3628,3628,3628,3628,3629,3629,3685,3685,3685,3685,3689,3689,3689,3689,3693,3693, 3693]
    print_artUnit_uspcClass(art_unit_list_3600, '705')
>>>>>>> 594292d3f82c4eae5d8f886b539a6fc5ed33b436

    example output:
    ...more art units printed but depricated view here for ease of reading...
    3689: 560
    3693: 592
    3693: 592
    3693: 592
    705: 162454
    '''
    artUnitCount = 0
    for unit in art_unit_list:
        print('{0}: {1}'.format(unit, len(df_oa[df_oa['art_unit'] == unit])))
        artUnitCount += len(df_oa[df_oa['art_unit'] == unit])
    print('{0}: {1}'.format(uspc_class, len(df_oa[df_oa['uspc_class'] == uspc_class])))
    print(artUnitCount-len(df_oa[df_oa['uspc_class'] == uspc_class]))
    
def column_values_to_string(dataframe, column_in_quotes):
    '''
    Input:
            dataframe: name of dataframe
            column_in_quotes: name of column to change any non-string values to strings.
    Output:
            none
            Changes any values in column that are not a string into a string.
    Example:
            column_values_to_string(df, 'code')
    '''
    dataframe[column_in_quotes] = dataframe[column_in_quotes].apply(str)

def create_df_with_class_705_706(dataframe, column_in_quotes):
    '''
    Input:
            dataframe: name of dataframe that has main codes 705 and 706.
            column_in_quotes: name of column where the main uspc code can be found.
    Output:
            Creates new dataframe df_705_706 with rows that contain 705 and 706 in the main USPC classification
    Example:
            create_df_with_class_705_706(df,'code')
    '''
    df_705_706 = dataframe[(dataframe[column_in_quotes] == '706') | (dataframe[column_in_quotes] == '705')]

def strip_class(dataframe, column_in_quotes):
    '''
    Input:
            dataframe: name of dataframe that has main codes 705 and 706. (does not accomodate codes that are less than 3 letters)
            column_in_quotes: name of column where the main uspc code can be found.
    Output:
            none
            Changes the column to only show the 3 letter code of 705 and 706
    Example:
            strip_class(df, 'code')
    '''
    dataframe[column_in_quotes] = [x[:3] for x in dataframe[column_in_quotes]]
