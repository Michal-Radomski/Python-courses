### What is `pipx`?

`pipx` is a command-line tool designed to help you **install and run Python applications in isolated environments**.

While standard tools like `pip` install Python packages globally or within a specific project environment, `pipx` focuses
exclusively on executable CLI tools (like Sherlock, Black, or httpie). It ensures that every application you install has its
own dedicated virtual environment. This keeps your global Python environment clean and prevents package version conflicts.

---

### Key Features and Benefits

- **Strict Isolation:** Every program installed via `pipx` gets its own private virtual environment. If two different tools
  require conflicting versions of the same dependency, they will never interfere with each other.
- **Global Accessibility:** Even though the tools are installed in isolated environments, `pipx` automatically adds their
  binaries to your system's `PATH`. This means you can run the application from any terminal window just like a native
  command.
- **Easy Upgrades and Uninstallation:** Updating or removing a tool is straightforward and clean, as deleting the app removes
  its entire private environment without leaving leftover files scattered across your system.
- **Run Without Installing:** You can execute a Python-based CLI tool temporarily without permanently installing it on your
  machine using `pipx run <package_name>`.

---

### How it Works (Comparison)

| Feature              | `pip` (Global)      | `pip` (Virtualenv)       | `pipx`                         |
| -------------------- | ------------------- | ------------------------ | ------------------------------ |
| **Primary Use Case** | Library development | Project development      | Installing CLI applications    |
| **Environment**      | Shared globally     | Manual setup per project | Automatically isolated per app |
| **Command Access**   | Easy                | Requires activation      | Globally accessible            |
