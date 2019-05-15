**RaspberryPiProjects**

Shared Repo With my Raspberry Pi Projects

**My notes on how to send changes from Surface to the RaspberryPi**
 >This should be easily

**From Surface:**
1. Make Changes
2. Save Changes locally (Ctrl + S)
3. Commit Changes using the `Git` plugin for Atom or GitHub desktop
    - Stage changes if in Atom. Not needed it using GitHub desktop
    - Input Commit Message
    - Commit to master (Ctrl + Enter) (_This is locally_)
4. Push changes in Git Bash (**Pushes to Remote**)
    - either use GitHub desktop app (_Ctrl + P_)
    - or use GitBash to push (`git push`) the changes

++++++++++++++++++++++++++++++++++++++++++++++++++++

**Pull changes to Pi:**
1. In command Line Interface, pull all Changes
    - cd to repository "RaspberryPiProjects" (`cd ~/RaspberryPiProjects`)
    - use command `git pull` to pull in Changes
2. Confirm changes are updated

Dont fuck it up.

====================================================

Not I need to figure out how to push changes _FROM_ the Pi.

1. Make Changes
2. Save Changes locally (Ctrl + S)
3. In CLI, commit all changes `git commit -a` 
     - or a specific file with `git add <file>`
4. with file stages, push wtih `git push`
