<img src=https://github.com/user-attachments/assets/5a10662a-e2e6-4670-a2ad-436f450d899c width="400"/>

## Summary

Python program for helping you learn by automatically opening a random selection of articles every day

**Constaints**:
- Once an article has been selected, it will be marked with an "*" so it won't be chosen again
- Unless there is only one site domain (e.g. www.martinfowler.com) left in the list of available articles, each selection will come from a different site domain

## Setup
### DailyDig
- Edit the list of available articles you'd like to read in the `articles.txt` file
- Change the number of articles you would like served by passing in an integer (e.g. 3) to the `open_random_articles()` method in `main.py`

### Cron Job
Schedule the articles to appear at your preferred schedule time by defining a cron job on your machine.

After cloning this repo onto your machine:

#### Copy the path where your Python/Python3 package is stored:
<img width="566" height="44" alt="Screenshot 2025-08-01 at 3 45 54 PM" src="https://github.com/user-attachments/assets/3d6517af-6f65-463b-a497-eff0bc9f8dd5" />

#### Copy the path where the dailyDig/main.py is
**From Terminal:**

<img width="383" height="32" alt="Screenshot 2025-08-01 at 3 59 54 PM" src="https://github.com/user-attachments/assets/dab320a8-db0f-4477-ab3c-793263520fef" />


**From Finder(Mac):**

<img width="324" height="244" alt="Screenshot 2025-08-01 at 3 49 19 PM" src="https://github.com/user-attachments/assets/ce460ae8-1aeb-4e84-b4cd-771f5241cb36" />

<img width="524" height="214" alt="Screenshot 2025-08-01 at 3 49 43 PM" src="https://github.com/user-attachments/assets/b4af8e21-4645-4b7c-af88-12868dea0be9" />

##### Create a cron command

From your crontab:
```
sudo crontab -e
```

Insert the following:

```
00 10 * * 1-5 {path_to_python} {path_to_dailyDig_repo}/main.py
```

this will set this program to run every weekday at 10:00AM, change to another time as needed (see [Cron Job Time Format](https://phoenixnap.com/kb/set-up-cron-job-linux))

### Misc.
If enough people are interested, I would be happy to expand this to include a .sh file that can automatically set this up for you or add other features/configurability. Let me know!
