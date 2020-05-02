import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """ 
    Drops all the tables in the database if they exist.
  
    Parameters: 
    cur (psycopg2 cursor): Database cursor
    conn (psycopg2 connection): Connection instance
  
    Returns: 
    None
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """ 
    Creates all the tables in the database if they don't exist.
  
    Parameters: 
    cur (psycopg2 cursor): Database cursor
    conn (psycopg2 connection): Connection instance
  
    Returns: 
    None
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """ 
    Main method used to drop and create all tables.
  
    Parameters: 
    None
  
    Returns: 
    None
    """
    
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()