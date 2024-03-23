# Questions

1. **Discuss your strategy and decisions implementing the application. Please, consider time complexity, effort cost, technologies used, and any other variable that you understand important in your development process.**
```
I employed Django and its inherent capability to establish relationships between tables within models as a strategic approach to achieve the application's desired outcomes. Additionally, I leveraged class-based views, envisioning the scalability of the project.

By implementing Django, I harnessed its ORM (Object-Relational Mapping) system to effortlessly define relationships between database tables through Python classes, thereby streamlining data management and enhancing the efficiency of the application's operations. Furthermore, the utilization of class-based views allowed for a more organized and modularized structure, facilitating future expansion and maintenance efforts.

Furthermore, the incorporation of a pandas-based CSV reader into the Django project allowed for efficient data ingestion and processing. While the time complexity of reading from a CSV file using pandas is typically O(n), where n is the number of rows in the file. 
``` 


2. **How would you change your solution to account for future columns that might be requested, such as "Bill Voted On Date" or "Co-Sponsors"?**

```
I would add date columns for votes and vote results, as well as co-sponsors in the bill models. The way I've implemented it makes it easy to add these attributes.
```

3. **How would you change your solution if instead of receiving CSVs of data, you were given a list of legislators or bills that you should generate a CSV for?**

```
I could use pandas to convert the list into a dataframe and then export to a csv
```

4. **How long did you spend working on the assignment?**
```
I spent about 3 hours on the assignment, making sure everything was correct. If I had more time, I would definitely improve the project's user interface, adding additional features to make it more intuitive and enjoyable to use. Additionally, I would dedicate time to optimizing the code, making it more efficient and easier to maintain in the future. I would also take the opportunity to conduct additional testing, ensuring that the project is robust and error-free.
```