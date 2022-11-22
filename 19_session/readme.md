# Disturbed Window Monsters
# K19 - Session Greetings
### Roster: David Chen, William Guo, Marc Jiang
### SoftDev
### Nov 4 2022
### Time Spent: 1.5

## DISCO
- Started session and saved username with 
```session["username"] = request.form.get("username")``` when username and pw were correct
- We can use different statuses to tell whether you were logged in or not and then use conditionals based on these statuses to change webpage
- Use ```session.pop(username)``` to pop the username from the session and therefore end it
- Can ```import redirect``` to redirect to /auth after logging out
- Can use conditionals depending on the method type to decide what to do