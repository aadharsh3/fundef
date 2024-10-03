class EmployeeDatabase:
    def __init__(self):
        self.collections = {}

    def createCollection(self, p_collection_name):
       
        if p_collection_name not in self.collections:
            self.collections[p_collection_name] = []
            return f"Collection '{p_collection_name}' created."
        return f"Collection '{p_collection_name}' already exists."

    def indexData(self, p_collection_name, employee_data, p_exclude_column):
        
        if p_collection_name not in self.collections:
            return f"Collection '{p_collection_name}' does not exist."
        
        for employee in employee_data:
            if p_exclude_column in employee:
                del employee[p_exclude_column]  
            self.collections[p_collection_name].append(employee)

        return f"Indexed {len(employee_data)} employees into '{p_collection_name}'."

    def searchByColumn(self, p_collection_name, p_column_name, p_column_value):
        
        if p_collection_name not in self.collections:
            return f"Collection '{p_collection_name}' does not exist."

        results = [
            employee for employee in self.collections[p_collection_name]
            if employee.get(p_column_name) == p_column_value
        ]
        return results

    def getEmpCount(self, p_collection_name):
        
        if p_collection_name not in self.collections:
            return f"Collection '{p_collection_name}' does not exist."

        return len(self.collections[p_collection_name])

    def delEmpById(self, p_collection_name, p_employee_id):
        
        if p_collection_name not in self.collections:
            return f"Collection '{p_collection_name}' does not exist."
        
        original_count = len(self.collections[p_collection_name])
        self.collections[p_collection_name] = [
            emp for emp in self.collections[p_collection_name]
            if emp.get('id') != p_employee_id
        ]
        return f"Deleted employee with ID {p_employee_id}. {original_count - len(self.collections[p_collection_name])} record(s) removed."

    def getDepFacet(self, p_collection_name):
       
        if p_collection_name not in self.collections:
            return f"Collection '{p_collection_name}' does not exist."

        department_count = {}
        for employee in self.collections[p_collection_name]:
            department = employee.get('department')
            if department:
                department_count[department] = department_count.get(department, 0) + 1
        
        return department_count



if __name__ == "__main__":
    db = EmployeeDatabase()

    
    print(db.createCollection("employees"))

    
    employees = [
        {"id": 1, "name": "Aadhi", "department": "HR", "age": 30},
        {"id": 2, "name": "mani", "department": "Engineering", "age": 25},
        {"id": 3, "name": "kani", "department": "HR", "age": 28},
        {"id": 4, "name": "Dani", "department": "Engineering", "age": 35},
    ]

    print(db.indexData("employees", employees, p_exclude_column="age"))
    print(db.searchByColumn("employees", "name", "Alice"))
    print("Employee Count:", db.getEmpCount("employees"))
    print(db.delEmpById("employees", 2))
    print("Department Facet:", db.getDepFacet("employees"))
