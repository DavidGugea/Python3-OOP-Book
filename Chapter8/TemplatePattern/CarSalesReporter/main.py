import sqlite3
import datetime

conn = sqlite3.connect("sales.db")


class QueryTemplate:
    def connect(self):
        self.conn = sqlite3.connect("sales.db")

    def construct_query(self):
        raise NotImplementedError()

    def do_query(self):
        results = self.conn.execute(self.query)
        self.results = results.fetchall()

    def format_results(self):
        output = []
        for row in self.results:
            row = [str(i) for i in row]
            output.append(", ".join(row))
        self.formatted_results = "\n".join(output)

    def output_result(self):
        raise NotImplementedError()

    def process_format(self):
        self.connect()
        self.construct_query()
        self.do_query()
        self.format_results()
        self.output_result()


class NewVehicleQuery(QueryTemplate):
    def construct_query(self):
        self.query = "SELECT * FROM Sales WHERE new ='true"

    def output_result(self):
        print(self.formatted_results)


class UserGrossQuery(QueryTemplate):
    def construct_query(self):
        self.query = "SELECT salesperson, sum(amt) FROM Sales GROUP BY salesperson"

    def output_result(self):
        filename = "gross_sales_{0}".format(datetime.date.today().strftime("%Y%m%d"))
        with open(filename, "w") as outfile:
            outfile.write(self.formatted_results)
