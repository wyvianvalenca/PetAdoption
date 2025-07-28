# PetAdoption
A system with classes for pets, shelters, and adopters, facilitating pet searches, adoption processes, and shelter management.

# Functional Requirements implemented during class in 25-07-16
- User Account Management: Users can create and manage their accounts;
- Pet Profile Management: Managing profiles for pets available for adoption;
- Shelter and Rescue Organization Profiles: Profiles for shelters and rescue organizations;
     > Listing all shelters was WIP
- Event Listing and Management: Listing events like adoption drives and fundraisers;
     > Updating events was WIP
- Educational Resources: Providing resources on pet care and adoption;
- Success Stories and Testimonials: Sharing success stories and testimonials from adopters;
- Community Forum: A forum for adopters and pet lovers to share experiences and advice.
     > Commenting and viewing comments was WIP

## Not implemented
- [ broken ] Search and Filter Options: Enabling users to search and filter pets based on various criteria;
- [ not attempted ] Adoption Application Processing: Handling and processing adoption applications;
- [ not attempted ] Donation Processing: Facilitating donations to shelters and rescue organizations;

## Updates

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

# Features

## Adopters:
- Create & Update Profile
- List Events
- List Shelters
- List Pets Up for Adoption
    - Filter pets based on various criteria
    - Apply to Adoption
- List Adoption Applications
- Social features
    - View Educational Resources
    - CRUD Success Stories
    - CRUD Forum Posts
    - Comment posts

## Shelters
- Create & Update Profile
- CRUD Events
- CRUD Pets
- List Adoption Applications
    - Respond Application
- Social features
    - CRUD Educational Resources
    - View Success Stories
    - CRUD Forum Posts
    - Comment posts

# TO-DO:

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
- [ ] Allow shelters to view received donations
- [ ] Change profile printing (use boxed_list())

## Bugs
- [ ] Pet status AVAILABLE FOR ADOPTION but no aplication form registered
    > ask for questions immediatly after changing status to AVAILABLE FOR ADOPTION
    > OR register standard form for all pets
- [ ] No system feedback after responding a application (success or failure messages)

## Extra (ideas)
- [ ] Filter events
- [ ] Order events by date
- [ ] Filter social posts
- [ ] Clean screen after each operation
- [ ] Allow adding standard question to all application forms in the shelter

# Author
Wyvian Valença
wgcv2@ic.ufal.br
