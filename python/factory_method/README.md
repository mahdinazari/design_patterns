### Factory Method Design Pattern
The `Factory Method` is a Creational design pattern used to instantiate objects without explicitly specifying their exact classes. This pattern delegates the responsibility of object creation to a specific method (typically called the Factory Method) within a class, allowing subclasses to determine which type of object should be instantiated. This approach enhances code flexibility and extensibility, as new object types can be added without modifying the existing codebase.

**Core Components of Factory Method**
- **Product:** An interface or abstract class that defines the characteristics or behaviors that the created objects must exhibit. This component establishes the generic type of the objects.  
- **Concrete Product:** Specific, concrete implementations of the Product interface or abstract class, which are instantiated by the Factory Method. These are distinct classes that encapsulate the actual logic.  
- **Creator:** An abstract class or interface that declares the Factory Method. This method is responsible for creating objects of the Product type but does not implement the creation logic itself, delegating that task to subclasses.  
- **Concrete Creator:** Subclasses of the Creator that implement the Factory Method, determining which specific Concrete Product should be instantiated.
Use Cases for Factory Method

**The Factory Method is particularly useful when:**  
**Flexibility in object creation is required**, and you want to avoid hardcoding dependencies on specific classes.  
You want subclasses to have the ability to specify the type of objects being produced.  
A system needs to support multiple similar object types, with the potential for these types to expand in the future.  
