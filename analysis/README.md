# Analysis for each table

`content` , `content_export` and `content_permission`

contains all information about project/challenge/concept .etc

The `object_id` corresponds to the object id in Table project/challenge/concept

`project`

e.g. https://launchforth.io/fuse/help-us-choose-the-next-challenge/team/

https://launchforth.io/api/v2/project/267/

`Project manager` is discribed in field `team` or `admins`

`project title`

project `id` and `title`

`project_action`

??

`project_image_gallery`

project images

`challenge`

challenges

`challenge_label`

?? but no use for us :)

`challenge_vote_categories`

different vote discreption for different challenges

`challenge_validation_item`

different challenge has different validation rules.

e.g. In https://launchforth.io/Alireza/dolph-bot/overview/  you'll find `You are missing multple requirements to be valid for voting. You have until the end of the validation period to make your adjustments and resubmit. View the validation spreadsheet here: https://docs.google.com/a/local-motors.com/spreads...` which is the category 4 for challenge 122.

`entry`

represent entries for each challenge. 

`id` is the entry id, `challenge` the corresponding challenge id, 'creator' field contains author info. `challenge_award` always null ??

`entry_revision`

contains images for each entry.

`entry_status_history`

who, when, submitted images/changes to which challenge. (activity history log)

`votes`

who vote for which entry in which challenge at which score.

`vote_category`

vote category

`malicious_voters`

which voter in which challenge is a malicious

`entry_validation_item`

??

`idea`

idea. `root_project` is the root project

`idea_image_gallery`

idea image galleries

`concept`

concept

`concept_revision`

concept images and status(Passed or Declined)

`concept_image_gallery`

concept image.

`blog_post`

discussion_topic is the topic. project is the project id it belongs to

`brainstorm`

brainstorm of some project

`task`, `task_media_list`, `task_media`

task of some project

`solution`,`solution_media_list`,`solution_media`

solution of some task




