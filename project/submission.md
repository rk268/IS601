<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Rupak Avinash Kulkarni (rk268)</td></tr>
<tr><td> <em>Generated: </em> 4/28/2023 11:24:00 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone1-deliverable/grade/rk268" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235038665-cf386397-6f20-4f2a-acc4-5a9e9b78efcc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 shows email validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235040965-608e2b69-a935-421a-a976-06176401f891.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2 Shows invalid password validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235040965-608e2b69-a935-421a-a976-06176401f891.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#3 passwords not much validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235040676-61df7b3d-6d77-4da6-bbd8-cb3ab8084b72.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#4 Screenshot email not available validation (already registered)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235041261-313177a5-f36f-495a-a3a5-704a58fac8a8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#5 Show username not available validation (username is taken)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235051620-622fed25-88ae-4e18-b478-1d1c725cbd08.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#6 form with valid data filled in before the form is submitted<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235051884-0f66842a-0fa4-4df7-b573-1434a9e00e39.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>valid user data from Task 1 should be present in this screenshot.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rk268/IS601/pull/29">https://github.com/rk268/IS601/pull/29</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>1)The FlaskForm class is used to generate a form class that inherits WTF.<br>This class defines fields, field types, and validations. Now, all we have to<br>do is access form fields and deliver the endpoint function's</div><div>request.</div><div>2) WTF forms on<br>the client side typically handle the internal validation defined in the custom form<br>class. However, we also use the WTF from function valid_on_submit() on the server<br>side to validate the form data once again. If any validation fails at<br>this time, validation errors are stored in the form object's errors field and<br>the form object is sent back to the frontend, where the validation error<br>is shown.</div><div>3) The password is first hashed whenever a new user registers, and<br>then the hashed value is stored in db</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235054654-1852565f-ac8d-40ea-9070-2646821d3f97.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show password mismatch validation.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235055080-d34af4e7-83c9-47b3-aa63-cba0089bc358.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>validation based on non-existing user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235055278-34bc1e2a-001e-45ab-b26b-2c31e59754d0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>flash message and/or a redirect to a landing page (post-login)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rk268/IS601/pull/29">https://github.com/rk268/IS601/pull/29</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>1. We can define a form class by inheriting from the FlaskForm class<br>in which we can specify the fields, field types, and validations. Then, we<br>can use this form object in our endpoint function to serve the request<br>by accessing the form fields.</div><div>2. The validations defined in the custom form class<br>are typically handled internally by WTF forms on the client-side. However, on the<br>server-side, we use the valid_on_submit() method of the WTF form, which again validates<br>the form fields. If any validation fails, the validation errors are stored in<br>the errors field of the form object, which is then returned to the<br>frontend where the validation error is displayed.</div><div>3. To enhance security, the password is<br>first hashed and the hashed value is then stored in the database. Whenever<br>a user tries to log in, the password entered by the user is<br>hashed, and this hash value is compared with the stored hash value in<br>the database.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235056320-a06c4ac3-8669-4449-ab0c-6efba709219b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Message saying successfully logged out.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235056691-38de4b29-5f60-4ed0-9e43-d2ea9ada7086.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Unauthorized message showing.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rk268/IS601/pull/29">https://github.com/rk268/IS601/pull/29</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div><div>Any time a user tries to visit a login-protected page, the session data<br>is checked to see if the user is authenticated; if not, the is_authenticated<br>flag remains false and the user is prevented from accessing the login-protected pages.<br>Basically, the session is set anytime a person logs in with their username,<br>email, password, and roles. The user will be able to access the login-protected<br>website during that period without having to log in since the session is<br>brief and only valid for 30 minutes.&nbsp;</div></div><div><br></div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235056691-38de4b29-5f60-4ed0-9e43-d2ea9ada7086.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Unauthorized message showing.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235058827-b0902f7b-4e41-4ed2-89ab-d4c6cd528219.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Message showing permission denied for unauthorized user.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235059092-69871052-964e-4929-a4cb-5a7f96a39cc4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>We see 1 record in roles table for Admin.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235059522-84a00f2f-0739-4bf1-8ec0-c59a4c85fb9a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The id 1 in the UserRoles table, is the admin.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235059748-f342d347-6485-40fd-b1e4-3b07cc71a52e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>rupakkul97 is the admin username.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rk268/IS601/pull/29">https://github.com/rk268/IS601/pull/29</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>Any time a user tries to visit a login-protected page, the session data<br>is checked to see if the user is authenticated; if not, the is_authenticated<br>flag remains false and the user is prevented from accessing the login-protected pages.<br>Basically, the session is set anytime a person logs in with their username,<br>email, password, and roles. The user will be able to access the login-protected<br>website during that period without having to log in since the session is<br>brief and only valid for 30 minutes.&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <div>Similar to login, user roles are stored in session data. If a user<br>tries to access a page that is protected by a role, access will<br>be denied because, according to the jinja template, certain functions are only accessible<br>and visible to admin users.&nbsp;</div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235062045-a4034027-a731-4c94-a275-ca697c95ffee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Navigation is styled<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235062173-13a78050-e401-4e15-b311-ec888a3c855d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Forms are styled<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235062502-7a6365e9-9850-4089-b14d-9b549c06650c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#3#4 UI does not have old artifacts and data displayed is in clean<br>manner.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rk268/IS601/pull/29">https://github.com/rk268/IS601/pull/29</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <div>The internal styling of the built-in form classes is utilized for styling. The<br>navigation class, whose styles are inherited, is used for navigating.</div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235063274-7148cd55-0374-443a-a5ae-1ee3baec6d6a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password doesnt match error<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235063429-217a8413-44c8-4a92-be38-32ae90bf9ca0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Duplicate username registration error message.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235064113-6cada121-2a72-4051-bec3-834205fc1c09.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Duplicate user email registration error message.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235058827-b0902f7b-4e41-4ed2-89ab-d4c6cd528219.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Permission denied error<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rk268/IS601/pull/29">https://github.com/rk268/IS601/pull/29</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <p>When an email or username already exists, a duplicate key error is generated<br>by the update/insert statement, which is then caught by the except block. In<br>the except block, a regular expression search method is utilized to determine whether<br>the duplicate word and the username/email are present. If they are present, a<br>user-friendly message is displayed stating that the username/email has already been taken.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235065397-0c348b66-fc72-4239-9643-e79ab5495020.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Proper validation is happening here.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rk268/IS601/pull/29">https://github.com/rk268/IS601/pull/29</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <p>When a user logs in, their data is retrieved from the session data.<br>This session data is then converted into a dictionary using the json.loads() function.<br>The dictionary items are then passed into the user object. Once the user<br>object is filled with the retrieved data, it is passed into the form<br>object. The data passed into the form object is then internally prefilled by<br>the WTF forms.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235066824-26f6f00b-8734-46ad-a0f9-c1b4f2cb91db.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>As I entered only 1 character it validates and tells to put more<br>chars.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235067029-966e20de-083a-4fbd-a626-b80a232f2227.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It is validating the wrong email id entered.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235177473-0035e837-96d8-4497-ac3c-bd857129f91d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password mismatch message is showing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235177797-3f13ac21-3438-44fa-aa2a-5fc79732edd7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email/username already in use message(duplicate entry error generated)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235179067-81de4cce-fe18-406f-befd-9b8fb66986ad.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>check user_id 9 its username is qwertytt<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235180512-ae6ac50f-3934-4e95-b764-a08f02a9e5b8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>check user_id 9 its updated to uop<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rk268/IS601/pull/29">https://github.com/rk268/IS601/pull/29</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <div>1)I have developed two distinct forms, one for modifying the username and email,<br>and the other for updating the password. 2)These forms have been implemented as<br>separate classes in the forms.py file and are displayed on the user's landing<br>page.</div><div><br></div><div>3)The username and email fields in the form are pre-filled with the session<br>data obtained from the login endpoint. When the user submits the form, their<br>entered username and email are checked against the old session data. If they<br>are the same, no changes are made. If they are different, an update<br>query is executed, and the session data is updated upon successful completion. In<br>case the user enters an existing username as their desired new username/email, a<br>duplicate key error is thrown, which is handled using an exception block and<br>a user-friendly message is displayed.</div><div><br></div><div>4)The second form is used for changing the user's<br>password. If the old password entered by the user does not match the<br>original password from the session, a friendly message is shown. Only if the<br>entered password matches the original password, the password is changed.</div><div><br></div><div>5)The form classes created<br>handle the validations, including checking for duplicate usernames or emails. In case of<br>a duplicate key error, a proper user-friendly message is displayed.</div><div><br></div><div><br></div><div><br></div><div><br></div><div><br></div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <div>During my project, I gained knowledge about the concept of sessions, which helped<br>me manage user logins and store data in sessions instead of querying the<br>database repeatedly for the same data. I also became familiar with user login<br>and logout mechanisms using the Flask_Login package and learned about roles in Flask<br>using the Flask_Principle package. Furthermore, I learned to use WTF forms, prefill them,<br>and add validations along with backend validation for input fields.</div><div><br></div><div>However, I encountered a<br>couple of problems. I noticed that although the username and password fields on<br>the user landing page were prefilled from session data, they did not update<br>when the user changed their username or email. To overcome this issue, I<br>updated the session data whenever necessary.</div><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-rk268-prod.herokuapp.com/">https://is601-rk268-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone1-deliverable/grade/rk268" target="_blank">Grading</a></td></tr></table>