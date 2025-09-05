# PetAdoption

A system with classes for pets, shelters, and adopters, facilitating pet searches, adoption processes, and shelter management.

# Getting Started

## Clone the repository and change into the project folder
```bash
git clone https://github.com/wyvianvalenca/pet-adoption-OO.git
cd pet-adoption-OO
```

## Create and activate a Virtual Envoirement
```
python -m venv venv
source venv/bin/activate
```

## Install the project dependencies
```bash
pip install -r requirements.txt
```

## Run
```bash
python app.py

```

# Functional Requirements

- User Account Management: Users can create and manage their accounts;
- Pet Profile Management: Managing profiles for pets available for adoption;
- Shelter and Rescue Organization Profiles: Profiles for shelters and rescue organizations;
- Event Listing and Management: Listing events like adoption drives and fundraisers;
- Educational Resources: Providing resources on pet care and adoption;
- Success Stories and Testimonials: Sharing success stories and testimonials from adopters;
- Community Forum: A forum for adopters and pet lovers to share experiences and advice.
- Search and Filter Options: Enabling users to search and filter pets based on various criteria;
- Adoption Application Processing: Handling and processing adoption applications;
- Donation Processing: Facilitating donations to shelters and rescue organizations;


# Features

## All Users
- Create & Update Profile
- Login
- Create account
- Access Social Feed (Educational Resources, Success Stories and Community Forum)
    - View posts
    - Like posts
    - Comment posts
- Post
    - Adopters can post Success Stories and Community Forums
    - Shelters can post Educational Resources and Community Forums

## Adopters
- List Events
- List Shelters
    - Donate to shelter
- List Pets
    - Filter pets based on various criteria
    - Apply to pet adoption process
- List Adoption Applications

## Shelters
- CRUD Events
- CRUD Pets
- List Adoption Applications
    - Respond Application


# Development Progress

## Functional Requirements implemented during class in 25-07-16
- User Account Management
- Pet Profile Management
- Shelter and Rescue Organization Profiles
     > Listing all shelters was WIP
- Event Listing and Management
     > Updating events was WIP
- Educational Resources
- Success Stories and Testimonials
- Community Forum
     > Commenting and viewing comments was WIP

### Not implemented
- [ broken ] Search and Filter Options
- [ not attempted ] Adoption Application Processing
- [ not attempted ] Donation Processing

## Updates after 25-07-16

### 25-07-18
- Adopters can list all Shelters
- Adopters can list all Events

### 25-07-19
- Adopters can list all pets
- Adopters can filter pets

### 25-07-21
- Shelters can add questions to pet's application form

### 25-07-22
- Adopters can apply to adopt pets (by answering adoption form)

### 25-07-23
- Shelters can view all applications to adopt their pets
- Adopters can view all their applications

### 25-07-27
- Shelters can respond adopter's applications (approve or deny) and provide feedback for denied applications.
- Better post printing
- Users can like and comment posts
- Users can see a post's comments and also like and comment a comment

### 25-07-29
- Adopters can donate to shelters
- Shelters can view their received donations
- Profile information is now printed inside a pretty box

### 25-08-02
- Fixed bug: no form for available pets
- Fixed bug: no system feedback after trying to process a form that's already been processed


# TO-DO

## Functional Requirements
- [ OK ] Allow adopters to search and filter peto
- [ OK ] Create application class
    > [ OK ] shelters can change pet's status to "available for adoption" 
- [ OK ] Allow shelters to write questions to ask adopters
    > [ OK ] shelters can define expected answers
- [ OK ] Allow adopters to apply to adopt
- [ OK ] Allow shelters to respond applications
    > [ OK ] shelters can view all adopters that applied to adopt a pet, and their answers, and the compatibility with expected answers
    > [ OK ] shelters can choose an adopter as tutor for a pet
- [ OK ] Allow adopters to all view their applications, compatibility rate and results
- [ OK ] Add initial posts
- [ OK ] Update post printing (use boxed_list)
- [ OK ] Allow commenting posts
- [ OK ] Allow liking posts
- [ OK ] Allow users to donate to shelters
- [ OK ] Allow shelters to view received donations
- [ OK ] Change profile printing (use boxed_list())

## Bugs
- [ FIXED ] Pet status AVAILABLE FOR ADOPTION but no aplication form registered
- [ FIXED ] No system feedback after responding a application (success or failure messages)
- [ KNOWN ] Duplicates in filter's options

## Extra (ideas)
- [ ] Allow choosing post type with code instead of typing
- [ ] Allow choosing pet filters with code instead of typing
- [ ] Document code
- [ ] Filter events
- [ ] Order events by date
- [ ] Filter social posts
- [ ] Clean screen after each operation
- [ ] Allow adding standard question to all application forms in the shelter


# Author
Wyvian Valença
wgcv2@ic.ufal.br
