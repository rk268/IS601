<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3  Business Management</td></tr>
<tr><td> <em>Student: </em> Rupak Avinash Kulkarni (rk268)</td></tr>
<tr><td> <em>Generated: </em> 4/22/2023 1:15:42 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-3-business-management/grade/rk268" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <div>Initial Preperation:</div><div><ol><li>Create two new dynos/VMs in Heroku:</li><ol><li>is601-ucid-mp3-dev</li><li>is601-ucid-mp3-prod</li></ol><li>Configure the heroku config vars and github secrets similar to how dev/prod were setup</li><li>Create two new secrets for github and set the values per the machine names in step 1</li><ol><li>HEROKU_APP_MP3_DEV</li><li>HEROKU_APP_MP3_PROD</li></ol><li>Duplicate your dev/prod yml files and have it listen to the mp3-dev and mp3-prod branches respectively</li><ol><li>Make sure you refer to the proper app secrets from step 3</li><li>You can merge these into regular dev/prod later but you'll want your final project to deploy over it (overwrite) on the normal dev/prod dynos/VM</li></ol><li>You can add this HW branch to the dev yml to test your deployments prior to the pull request to dev from step 4</li></ol></div><div><br></div><div><br></div><ol><li>checkout dev and pull any latest changes</li><li>Create a branch called mp3-prod and immediately push it</li><li>Create a branch called mp3-dev and immediately push it</li><li>Create a branch called MiniProject-3</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li><b>Immediate add/commit/push to github</b></li><li>Open a pull request to mp3-dev and keep it open until you're done adding the submission file</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li><li>&nbsp;pytest BusinessManagement/test/name_of_test.py -rA</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item and add a related commit message for clarity)<br></li><ol><li>Do not delete any provided comments</li></ol><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 10</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together and reuse the image</li><li>Ensure all screenshots are properly captioned in the deliverable section so it's clear what part you're trying to show</li></ol><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from mp3-dev to mp3-prod and merge it</li><ol><li>If you want to keep original dev/prod up to date you can merge the changes into those, but they will cause a deploy to occur for each so be mindful</li></ol><li>Navigate to the submission file under the BusinessManagement folder from mp3-prod</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>Some files will have "DO NOT EDIT" mentioned, please don't edit these. If there's a doubt about any of them ask.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>If a test case isn't possible to complete, capture the failed test case locally via `pytest BusinessManagement -rA` first, then you can rename the function to `off_original_name`.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div>Note: db.py has been updated to use pymysql instead of mysql-connector-python to aid in easier queries.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>May want to download branch as a zip, then copy/paste the files into your repo (if/when you do, please immediately do a git add/commit to record the baseline items)</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233181313-e95f525d-c841-4b42-aa02-bb858f2c8e2f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1DIAR-mt85 updated to DIAR-rk268 <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233181655-2d65c9d1-886c-4419-a57d-a787f83136f7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#3 brought to you by message updated.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233682223-ea8f6774-3d10-40f7-9f52-3d7a35ba070c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2 successfully deployed on heroku dev. Hence the link is visible.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233682223-ea8f6774-3d10-40f7-9f52-3d7a35ba070c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#4 #5 relevant URLS added for company search and company add<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233685137-2e810842-550a-4b00-9227-3139da77b0e4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#6#7 relevant URLS added for employee search and employee add<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233684924-ee046319-e579-4b25-9f0a-c6b2ef1a546c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#8 relevant URL added for admin import.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233685415-af3c89ca-dbc5-4236-84ec-d3545fd2cb63.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 IS601_MP3_Companies table visible<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233796238-e631057f-b844-4781-a3e1-01d07a4aa0d3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2 IS601_MP3_Employees table visible<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route (code)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/230741110-2e07fc3d-40da-4e52-a108-f101183babda.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#5 #6 len employee  telling how many records were processed. if the<br>list is empty proper flash message is visible.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233685986-f04e8893-1c89-43f2-b9c0-f1a36611302f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 code is properly checking the file format.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233686405-bff74a14-c209-4c13-a26a-80d2854a205a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2 	CSV file is reading from the provided stream as a dict<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233686658-451e4949-9498-4423-bb4a-2b2d88bc5150.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#3#4 employees and companies are successfully appended as dict.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233796670-d5390d3b-c089-427a-b4eb-843fb072a3cd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 and #2 proper success message are visible as expected.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233796498-534ddb5f-f9d2-40e2-9489-a5de6f3ab7ae.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#4 shows proper flash message when the file is not attached.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233796604-f4a17d87-b4c2-448b-b5a6-d8e492c22e33.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#3 showing proper message when the file is not a csv file.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/230744191-f2d5218a-1eca-4599-9ff3-7dcfad24fd7c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1  screenshot showing some employee data was uploaded<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/230744264-ffaeb4b2-57dd-4fbe-bda9-ecb397e73667.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2 screenshot showing some company data was uploaded<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233751299-f45c427b-fae6-42a2-b390-17475cdbf053.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1#2#3#4#5#6 code properly getting first_name, last_name, company (id), email, and if any field<br>is not entered then respective flash error messages are seen. Email validation is<br>also present.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233751422-fb638a70-d9bf-4df1-9be8-b774872535e4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#7#8#9#10 proper insert query written with the except block with the flash message<br>visible.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233751672-9102aaf7-2e57-46ca-92bc-06632ff00b29.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot has all the fields entered prior submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233751726-a1311cff-dae2-4118-b2aa-46458fc45f94.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows data created employee record<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233752630-8c2d067a-7705-4719-94bd-6819f0500357.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shoes the error message if the first name field is empty<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233752712-f5a155e7-dd0c-4d0e-854e-3e70e5b28c36.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shoes the error message if the last name field is empty<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233752786-22c5d1f1-bc32-417d-8adc-a5795131c48e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shoes the error message if the email  field is empty<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233752995-7ae893f7-46b4-42ad-9a31-a9ba4f2a7077.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot shoes recently added(Rupak(my name) entry recently added). also previously added fields<br>are also seen. Please check id 2081 for checking this entry.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/230802989-e72da0dc-024f-483c-8580-7c92755d102b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 select query filled in properly.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233753281-bb1b8f9c-99c9-4fcc-83eb-42d099fbf5aa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Checked request args for fn, ln, email, company, column, order, limit with exact<br>naming<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233753356-52d79bff-02b6-4fd6-9bc1-1749117f2393.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>respected filters appended for the first name, last name, email and company id.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233753525-68cb1982-966d-44d9-b3ef-9dd28502f5d0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#7#8#9( for #7 sorting done by order by in asc, dsc . for<br>#8 appended required limits for the entered values. for #9 with proper error<br>message for out of bound index.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233753711-53f6122e-5ee8-44ba-af1d-48ba81dc9ce8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#10 Except block has a user friendly message flashed and a print() of<br>the exception.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233753887-44f8e3ab-9667-4954-a07a-1f443910ba64.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows results with last_name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233753930-71a0f21a-feae-456b-bfa2-ce15e20739d6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows results with first_name filter applied;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233754101-4e2ab4f1-c32b-411e-93fc-10371b022b91.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows results with email filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233754026-9ee0232c-fdbb-4e32-867f-27fb244c979c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with company filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233754172-a11be3af-0ea3-46eb-ac66-34b89a54c744.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show one asc filter applied (last namecolumn was chosen) up is asc<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233754215-5f9e2847-211c-4954-98d1-3e73bd4b0c08.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show one desc filter applied(last name column was chosen) down is desc<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233754723-2a1da5e2-70dd-44da-b61b-e9181ce97db8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1#2#3#4(#1 The code gets the required values from the form.get and checks if<br>they are null or not. If they are it gives a proper flash<br>message except for company.)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233754749-9a3b164e-04b5-4325-86e8-e9003b67fb02.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email is checked with its format.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233754853-a2403184-2e61-47f5-ae86-054d8faaf044.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#6#7(#6 proper update query is visible. #7 Both the flash messages are visible)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233754913-e5c5e0e6-3093-49ee-a9b4-15a29c835228.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#8#9(#8 Select query is visible and #9 Employee data is passed to render<br>template.)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233754947-cce5607e-95c2-4dc2-9e0f-aa64278ed0fd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>consider item 2060 item. (Rupak) before edit.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233755477-88ddb83d-987d-4d15-8478-cc62f3f1e205.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2 going to edit number 2060 with this info<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233755521-d69ae3f0-4f24-4b94-8109-945e694c84b0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2  The record has now been updated<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233755539-0230bd26-d1bb-4698-b64b-31e39b3bb621.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2#3 As you can see item id 2060 has been edited /updated as<br>thought.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233755624-2a73e84c-fc3f-4a71-9066-7b4488aba8e0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Lets consider id as 2067 Shawna. and edit it.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233755679-652fb86f-f52f-44a9-bdb6-27f75348030a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>going to update 2067 with this info.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233755716-47c40060-cd49-45c6-aec3-f1ff964ff270.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>please check item 2067 has been updated as expected.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233755913-b31056b2-52f5-4624-bfa4-838764026c76.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1( request.form.get is getting the required values). #2#3#4 Name address city are required<br>else flash message is displayed. <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233756202-54ec6e3c-15dd-425e-b6a3-4b79588edda0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#5#6#7#8#9#10 State country zip are required and validated. website is not compulsory hence<br>not validated. If required things are not there then flash error message is<br>displayed.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233756316-92777f24-e59e-4f6e-96f0-2ed2f3de34c2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#11#12 Proper insert query is there with the required flash messages in the<br>if (which is in try) and the message in the except is also<br>there.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233756445-7a6a25c6-7e0f-4067-b5fc-88c8f41b8d83.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 filled in prior data visible<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233756486-df56e693-7552-4b3e-9e00-e7e8e0c1f9fa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2 added company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233756637-cf38988e-adda-4288-8d21-f2f1bafd2b82.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>name error message is visible<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233756637-cf38988e-adda-4288-8d21-f2f1bafd2b82.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Please enter name message is visible.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233757010-38d7213d-f143-43bf-8ba7-0900046e5661.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>address error message visible<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233757088-f1c75613-62f3-440b-b38f-4c634f304e8c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>city error message visible<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233757522-2cb1d6b2-83f4-4625-ac9a-dd750c0ad946.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>state error message visible<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233757574-0ab4c304-035d-49bd-a88d-a30ef1608d58.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>country error message visible<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233759952-1d385235-752e-4c16-a91b-fbbc75f028c4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>zip error message visible<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233757758-c9d01b31-65b7-45c3-87ff-13898d432651.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot before adding company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233757839-9cdc22ff-2245-427d-9445-bfa32a9ab060.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Added company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233757871-839f2cb7-9dc3-4876-83d1-a51c4c79f65f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>3044 entry shows aarohi events added as a company<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233758209-7b3b97f0-6fb3-4a12-b903-544fc739d1c7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>select query for company search.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233758236-e5f0c6d8-0091-4b92-ac67-9ec657ed2e54.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>args get getting name, state, country, coloumn, order, limit <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233758309-ef980492-2961-4d57-88c5-bff62c1300af.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#3#4#5 appended the necessary filters for the fields name,country, state<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233758405-e06d19c2-5ef2-42e4-a5a5-59dcd28100e9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#6#7#8(#6 appended sorting if column and order are provided and within the allows<br>columsn and allowed order asc,desc allowed_columns = [&quot;name&quot;, &quot;city&quot;, &quot;country&quot;, &quot;state&quot;], #7 appended<br> limit as expected. #8 limit with proper message if its going out<br>of bound<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233758546-5de8be68-148d-483e-9947-3a0e87bc252e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#9 if the result.status  has something (if the select all query is<br>returning something then its printing THE ROWS if the status is false, then<br>it gives the exception with the flash messages as expected.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233758857-c2654dad-7f56-4930-9866-b0be4143966e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>results with name filter applied;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233758922-6e421363-374d-4270-857a-2d9a3c2ac86e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> results with country filter applied;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233758999-a959068b-3200-4176-853d-5f4e1aaad087.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>results with state filter applied;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233759080-f7c1e54d-e3b7-4bd7-b6a8-e7c115f3bed7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here I have selected country field. As You can see up means asc.<br>Hence its giving countries from a to z as per the database entries.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233759188-edc2c878-7c26-48d5-8c38-2ceccb67c018.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here I have selected country field. As You can see down means down.<br>Hence its giving countries from z to a  as per the database<br>entries.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233759446-8f5b7d68-8513-4533-a342-efe395ee4abf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code is retrieving  id (from request args) name, address, city, state, country,<br>zip, website from form.  flash messages are  related error message and<br>redirect to company search.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233759744-fa3ad71c-160d-42e7-804c-12058de7e4b1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2#3#4#5#6#7#8(All necessary fields are checked such as name address city state country <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233760018-e0dd8105-3f02-4a8d-9a3b-2122fa6a3f52.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#9#10 (#9 Proper UPDATE query is visible with the passed data. #10 Except<br>blocks (two) have user friendly message flashed and a print() of the exception.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233760092-396f3971-21b0-4fb7-bc90-b1e25af69111.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#11#12(#11 Proper SELECT query is visible with the passed in data. #12 Company<br>data is passed to the render_template()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233760295-31070b81-a0b8-4d0e-8afa-6265d7debb47.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1  data before an edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233761169-d5e78a79-b506-4a2f-b94d-f4abe6712473.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Going to edit the original data with this information.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233761198-da497aac-a4f8-432a-8e52-29d5ce0a7d7b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Check 3 action item its updated/edited<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233760327-245981d5-2e0f-435b-bc04-660d527ae8e6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Initially the the original data is the checked checkbox in the screenshot. Now<br>I am going to edit the data at that position.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233761280-e9135fc9-fbd8-4c88-9437-3947dc2d49da.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The item which need to be checked has been checked(checkbox checked). hence we<br>see that the data base has also updated the record.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233761531-8ff3401d-3f5f-4973-903c-a2c041552051.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>request.args gives the id which is then passed to the query to delete<br>the entry. If theres any issue in query or fetching the id proper<br>error flash message is seen else the success message is seen. At the<br>end the page is redirected to the employee search URL.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233761767-d07d891f-0d81-4b92-9e52-47b3762e6cb8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Going to delete 1st entry Action 1 James butt.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233761798-2f9aebc0-729b-4984-9a2c-ae54ea29575c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After clicking on delete.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233761826-948eb19b-924e-4d97-aef0-993f97fa405a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After the deletion. we see that the action 1 (James butt has been<br>deleted)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233762310-da05041d-7add-40b7-ba5c-83f081c8402c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>request.args gives the id which is then passed to the query to delete<br>the entry. If theres any issue in query or fetching the id proper<br>error flash message is seen else the success message is seen. At the<br>end the page is redirected to the company search URL.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233762379-25823173-55c4-41fc-9e90-bbe3770c19eb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Going to delete 1st entry Action 1 yjtrsj<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233762405-db7db25a-7861-4d7b-9b7f-e4cb129e5597.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After clicking on delete.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233762448-70fcd98a-77bb-41d7-93cf-2aadf6ec810f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After the deletion. we see that the action 1 (yjtrsj has been deleted)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233762473-9282a6d3-35da-42f3-827d-3448a1ab5d06.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After the deletion. we see that the action 1 (yjtrsj has been deleted)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233797067-74392310-37bc-4111-93c7-0016cf1dbb7c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshots of number of test cases passed and failed. <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/233797487-311cec91-0cf4-4631-8f01-5c9b35a102c9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshots of number of test cases passed and failed. <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <div>I learnt how to combine Python code with HTML files, and the other<br>way around.</div><div>Python, HTML, and Jinja all became more clear to me.</div><div>I gained knowledge<br>on how to use Flask to create a website and how to use<br>the front end of a database to access data.</div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-3-business-management/grade/rk268" target="_blank">Grading</a></td></tr></table>