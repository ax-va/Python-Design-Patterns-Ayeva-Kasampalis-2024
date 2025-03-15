## Performance Patterns

### Cache-Aside

When data is more frequently read than updated, applications can use a *cache*
to optimize repeated access to information stored in a database or data store.
In the *Cache-Aside* pattern, frequently accessed data is stored in a cache, 
reducing the need to fetch data from the data store repeatedly.
The cached data usually exist for a relatively short period of time.

### Memoization

The *Memoization* pattern is used if a function is called with the same inputs more than once.
Results of expensive function calls are cached to avoid repetitive and costly computations, 
significantly reducing execution time.

### Lazy Loading

The *Lazy Loading* pattern is used to defer the initialization or loading of resources 
until they are actually needed.
