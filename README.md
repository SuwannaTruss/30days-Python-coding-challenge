<div align="center">  
  <h1>30days Python Coding Challenge</h1>

  <a href="#" title="header">
    <img
      height="80"
      width="80"
      alt="Python icons created by Freepik - Flaticon"
      src="https://cdn3.iconfinder.com/data/icons/logos-and-brands-adobe/512/267_Python-512.png"
    />
  </a>
</div>

<hr/>

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Rules](#rules)
- [Why should we do it?](#why-should-we-do-it)
- [Accepting a Challenge](#accepting-a-challenge)
- [Forking a repository](#forking-a-repository)
- [Cloning your forked repository](#cloning-your-forked-repository)
- [Adding your solution](#adding-your-solution)
- [Resources](#resources)
## Rules
- Do one challenge (or as many as you like) a day for 30 days in a roll.
- Commit your code on github.
- A choice of coding challenge and level are entirely yours. ie. [codewars](https://www.codewars.com/collections/python-practice-1), [HackerRank](https://www.hackerrank.com/domains/python)

## Why should we do it?
- Participating in a coding challenge can enhance your coding skills.
- Consistency is the key to success, and a coding challenge can help build that consistency.
- Joining a coding challenge can help you connect with like-minded individuals.
- A coding challenge can provide the motivation you need to stay focused and productive.
- Completing a coding challenge can showcase your skills to potential employers.

## Accepting a Challenge
You can start your 30 days streak journey by 
- Fork my repository to quick start yours (see instructions below).
- Create your own own repo from scratch, followed the instruction in [this YouTube](https://www.youtube.com/watch?v=aoBOUmO4QP0).
  
## Forking a repository

- On GitHub.com, navigate to the [30DAYS-PYTHON_CODING_CHALLENGE](https://github.com/SuwannaTruss/30days-Python-coding-challenge) 
- In the top-right corner of the page, click **Fork**.
- Select an owner for the forked repository. ie. your personal github account.
- Click **create fork**

## Cloning your forked repository
To get this forked repository in your local workstation. 
- On Github.com, navigate to **your fork** of the 30DAYS-PYTHON_CHALLENGE repository.
- Above the list of files, click **Code**
- Copy the URL for the repository
- Open Git Bash on your workstation.
- Make sure that you are in the preferred working directory.
- Execute 

```bash
$ git clone <the copied URL>
```
- Your local clone will be created.
- (optional) you can also open the folder od this repository in VS code, execute
```bash
$ code .
```

## Adding your solution
Add your solution every day for 30 days.

**Step #1** - open your editior ie. VS code
- From file menu, select open the folder
- Open `30-DAYS-PYTHON-CODING-CHALLENGE` folder from your directory.

**Step #2** - before you add your code.

*Using Explorer in VS code*
- Create sub-folder, named with `day<number of days>` ie. `day1`, `day2`
- Create a new file for each solution in this new folder.

*Using terminal in VS code*
- From Terminal menu, In VScode, open new terminal
- To create a new folder, execute select new terminal
- To create new folder, excute 
```bash
mkdir day<number of days>
```
- To change directory into that folder, execute
```bash
cd  day<number of days>
```
- To create and open a new file, execute
```bash
code <solution name>
```

**Step #3** - add your code in the file
- You may want to add the link to your challenge and the instruction for future reference.
- Add your code
- Save the file

**Step #4** - commit your file(s) to your local repository
- Open a new bash terminal on your VS code
- To check changes, execute
```bash
$ git status
```
- To stage all changed files.
```bash
$ git add .
```
- To commit all staged files to local repository
```bash
$ git commit -m "<your message>"
```

**Step #5** - commit to your remote repository on GitHub
- Execute
```bash
$ git push
```

## Resources
**Git and GitHub**
To learn more about Git and GitHub, I recommended this *Git and Github Hands On Workshop* series on YouTube by WomenWhoCode
[Session 1](https://www.youtube.com/watch?v=4nHtEeeuWhA&t=2s)
[Session 2](https://www.youtube.com/watch?v=f4_x2nfNYe4)
[Session 3](https://www.youtube.com/watch?v=qfiBkO9bFdc&t=4241s)

**Forking a repository**
[GitHub Documentation](https://docs.github.com/en/get-started/quickstart/fork-a-repo).

