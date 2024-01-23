# Gomibo Hackathon 2024 :office: :computer: :crown:
<img src="https://werkenbijbelsimpel.nl/wp-content/uploads/2023/01/Belsimpel-A-Gomibo-company_RGB_op-wit.svg" width="300" height="150">

## Installation guide
This section contains all relevant information to setup the necessary things to participate in the hackathon. You will be setting up a Docker environment running two services: MySQL and PHPMyAdmin. We've created a docker-compose.yml file which should do most of the work for you.

### Clone Github repository
Start by cloning the Github repository on your device. Most of you will probably have done this before, but if not we highly recommend the following **before** cloning the repository.
1. Create a Github account --> [Sign up here!](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home)
2. Add SSH token to your account --> [How do I do that??](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
3. Install Git on your device --> [More instructions!](https://github.com/git-guides/install-git)

Now you should be ready to clone the repository:
1. Navigate to a folder on your device where you would like to clone the repository into.
2. Clone the repository.
```
git clone git@github.com:belsimpel/hackathon2024.git
```
3. Navigate into the repository.
```
cd hackathon2024
```
4. You should now see the project files!

### Setup credentials
1. Open the hackathon2024 directory on your favorite IDE.
2. Edit the `.env` environmental file. You should add some credentials.

### Start Docker container
1. Now it's time to start spinning up the Docker environment.
2. First up, read through this installation guide for installing Docker and Docker Compose.
3. In a terminal, move to the projectfolder again (hackathon2024).
4. Pull the latest images.
```
docker-compose pull
```
5. Start the docker environment.
```
docker-compose up
```
*Tip, add the `-d` flag to run the container in the background.*

6. Go to http://localhost:8081/ and you should see PhpMyAdmin! You're now good to go. :finish:

### Shutting down
1. To shut everything down, just enter the following in your terminal.
```
docker-compose down
```

### Assignment
When you clone the repository you will also find the assignment in your directory which will be locked by a password. On the day of the hackathon, you will receive the password. Make sure to ready through the assignment carefully!

### Working together
How you work together is up for you to decide, but we recommend setting up a Github repository. You should already be assigned to a team, please contact each other and discuss how you want to work together. It might save time to set up a Github repository already so you can start working on the assigenment as soon as possible.