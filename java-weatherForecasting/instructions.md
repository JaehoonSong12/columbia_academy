# Gradle Commands for Windows

Here’s a rundown of the most common Gradle commands you’ll run on Windows (using the built‑in wrapper `gradle`). You should run these from your project’s root directory in a Command Prompt or PowerShell.

## 1. Project Initialization & Wrapper

- **Initialize a new project**  
  ```bat
  gradle init
  ```
- **Generate (or update) the Gradle wrapper**  
  ```bat
  gradle wrapper
  ```
  This creates (or refreshes) the `gradle` and `gradle/wrapper/` files.

## 2. Inspect & Discovery

- **List all available tasks**  
  ```bat
  gradle tasks
  ```
- **Show all project properties**  
  ```bat
  gradle properties
  ```
- **Print dependency tree**  
  ```bat
  gradle dependencies
  ```

## 3. Build Lifecycle

- **Clean your build directory**  
  ```bat
  gradle clean
  ```
- **Compile & assemble binaries**  
  ```bat
  gradle build
  ```
- **Only compile (no tests or packaging)**  
  ```bat
  gradle assemble
  ```
- **Run all checks (compile, tests, code quality, etc.)**  
  ```bat
  gradle check
  ```

## 4. Testing

- **Run unit tests**  
  ```bat
  gradle test
  ```
- **Run a specific test class**  
  ```bat
  gradle test --tests com.example.MyTestClass
  ```

## 5. Running Your App

*(Requires the [application plugin](https://docs.gradle.org/current/userguide/application_plugin.html) in your `build.gradle`.)*

- **Run the main class**  
  ```bat
  gradle run
  ```

## 6. Packaging & Publishing

- **Generate a JAR**  
  ```bat
  gradle jar
  ```
- **Publish to a Maven/Ivy repo**  
  ```bat
  gradle publish
  ```

## 7. IDE Integration

- **Generate Eclipse project files**  
  ```bat
  gradle eclipse
  ```
- **Generate IntelliJ IDEA project files**  
  ```bat
  gradle idea
  ```

## 8. Advanced & Troubleshooting

- **Enable stacktrace on failure**  
  ```bat
  gradle build --stacktrace
  ```
- **Enable full debug log**  
  ```bat
  gradle build --debug
  ```
- **Profile build performance**  
  ```bat
  gradle build --profile
  ```
- **Daemon control**  
  - Stop all daemons:  
    ```bat
    gradle --stop
    ```
  - Check daemon status:  
    ```bat
    gradle --status
    ```
