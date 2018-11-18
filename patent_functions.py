


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
    art_unit_list_for_706 = [2121, 2129]
    art_unit_list_for_705 = [3622,3623,3623,3625,3625,3626,3627,3627,3627,3628,3628,3628,3628,3629,3629,3685,3685,3685,3685,3689,3689,3689,3689,3693,3693, 3693]
    print_artUnit_uspcClass(art_unit_list_for_705, '705')

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
    


#drop duplicates
#df_oa_2015_start['app_id'].value_counts(dropna=False)