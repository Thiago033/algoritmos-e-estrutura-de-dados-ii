import pandas as pd
    
def main():
    # my_dict = {'Dave':'001', 'Ava':'002', 'Joel':'003'}
    # my_dict = dict(Dave='001', Ava='002', Joel='003')
    
    emp_details = {'Employee': 
                    {
                        'Dave':{'ID':'001', 'Salary':'1000', 'Designation':'Team lead'},
                        'Ava':{'ID':'002', 'Salary':'2000', 'Designation':'Team lead'}
                    }
                }        
        
    
    df = pd.DataFrame(emp_details['Employee'])    
    print(df)
    
        
if __name__ == "__main__":
    main()