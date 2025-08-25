This is a subdirectory for Taiyun to work on Georgia Tech lecture contents.

In windows, start your vscode by double clicking `.start.bat` file!

For `Oracle` Java distro, use the following javafx library. `Julu` distro already has JavaFX framework embedded!
```
https://jdk.java.net/javafx21/
```


# Installing Java Guide (JDK 11)

## Windows
- Uninstall any existing versions of Java (if any) on your PC.
- Download and install: https://cdn.azul.com/zulu/bin/zulu11.60.19-ca-fx-jdk11.0.17win_x64.msi
- Restart your PC.
- See HW0 for steps to check if it is correctly installed.
- If steps did not work (usually shows some Java but not the expected one), follow these steps to change the JVM:
  - Note the installation path of the JDK (e.g. `C:\Program Files\Java\jdk11`).
  - You can either do **A** or **B**:

  **A.** Use the `setx` command as so (replace the path with your installation path):

  ```powershell
  setx JAVA_HOME "C:\Program Files\Java\jdk11" /m
  ```

  **B.** Update your `PATH`:
  1. Type "env" into search.
  2. Click **Edit environment variables**.
  3. Click **Environment variables** at the bottom.
  4. Under **User Variables**, select **Path**.
  5. Click **Edit**.
  6. Add a new line (**New**).
  7. Add the installation path noted earlier, then add `\bin` to the end.
  8. Save and close environment variables windows.
  9. Restart your PC.

- Consult with TAs if steps did not work.

---

## Mac
- Download and install:
  - For **Intel-based Macs** (NOT M1 / M2 / M3):  
    https://cdn.azul.com/zulu/bin/zulu11.60.19-ca-fx-jdk11.0.17-macosx_x64.dmg
  - For **Apple Silicon Macs** (M1 / M2 / M3):  
    https://cdn.azul.com/zulu/bin/zulu11.60.19-ca-fx-jdk11.0.17macosx_aarch64.dmg
- Restart your Mac.
- See HW0 for steps to check if it is correctly installed.
- If steps did not work (usually shows some Java but not the expected one), follow these steps to change the JVM:  
  https://medium.com/@devkosal/switching-java-versions-on-macos-80bc868e686a
  - Include step 5 from that guide, but instead of adding it to just `~/.bash_profile`, add it to (or create) `~/.zshenv` as well.
- Consult with TAs if steps did not work.

---

## Linux (and any other OS)
- See https://www.azul.com/downloads/?version=java-11-lts&package=jdk-fx for an appropriate version that corresponds to your machine’s operating system and architecture.  
  - **Do not** change the filters for **Java Version** and **Java Package** from the ones autocompleted from the link.
- See HW0 for steps to check if it is correctly installed.
- If on Linux and steps did not work (usually shows some Java but not the expected one), follow these steps to change the JVM:  
  https://askubuntu.com/questions/740757/switch-between-multiple-java-versions/740782#740782
- Consult with TAs if steps did not work.
