import yaml,requests,os,time
import sqlite3
if __name__=="__main__":
    root_path = os.path.dirname(os.path.dirname(__file__))
    db_f_path = os.path.join(root_path, 'galaxy_tools.db')
    con=sqlite3.connect(db_f_path)
    c=con.cursor()
    tool_id=1
    #c.execute('select* from TOOLS where ToolID=?',(tool_id,))
    #c.execute('select * from TOOLS')
    #c.execute('select * from PARAMETERS')
    c.execute('select * from FILES')
    values=c.fetchall()
    print(values)
    #print(values[0][1])
    con.close()