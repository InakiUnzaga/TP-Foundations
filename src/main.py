import pandas as pd
import psycopg2

def main():
    print("Prueba 123")

    #prueba de pandas
    df = pd.DataFrame({
        'col1': [1, 2],
        'col2': [3, 4]
    })
    print(df)



if __name__ == "__main__":
    main()