### Proxy Design Pattern
The Proxy design pattern is a `Structural pattern` that provides a substitute or intermediary (surrogate) for a real object. This pattern allows the client to interact with the object through a Proxy rather than accessing the real object directly. The Proxy typically implements the same interface as the real object and can handle tasks such as access control, optimization (e.g., Lazy Loading), or adding supplementary functionality (e.g., logging) without the client noticing any difference. The main types of Proxy include Virtual Proxy (to delay object creation), Protection Proxy (to regulate access), and Remote Proxy (to access objects in different systems).

#### Core Components of Proxy
**Subject:** An interface that both the real object and the Proxy adhere to, defining the executable operations.  
**Real Subject:** The actual object that implements the core functionality, which the Proxy references.  
**Proxy:** A class that implements the Subject interface and acts as an intermediary. The Proxy forwards requests to the Real Subject and may apply additional logic.

#### Use Cases for Proxy
**Lazy Loading:** When creating the real object is resource-intensive (e.g., database connections or loading large files), and you want to defer its instantiation until it’s needed.
Access Control (Protection Proxy): When you need to restrict access to an object (e.g., checking permissions before performing operations).  
**Remote Access (Remote Proxy):** When the object resides in another system, and the Proxy serves as a local representative (e.g., in distributed systems).  
**Logging or Monitoring:** When you want to perform additional operations, such as logging, without modifying the real object.

#### Advantages
Reduces resource consumption by delaying the creation of heavy objects.  
Adds a layer of control or extra logic without altering the real object.  
Transparency for the client (no changes required on the client side).  

#### Differences from Other Patterns
Unlike the Adapter pattern, which adapts incompatible interfaces, the Proxy maintains the same interface as the real object and focuses on managing access.  
Unlike the Decorator pattern, which adds new functionality, the Proxy typically emphasizes control or optimization rather than enhancing behavior.  

This pattern is highly practical in scenarios requiring resource management or precise control over object access.  