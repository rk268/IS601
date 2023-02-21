<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - Tracker App</td></tr>
<tr><td> <em>Student: </em> Rupak Avinash Kulkarni (rk268)</td></tr>
<tr><td> <em>Generated: </em> 2/20/2023 9:32:04 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-1-tracker-app/grade/rk268" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout dev branch and pull any pending changes&nbsp;</li><ol><li>&nbsp;git checkout dev</li><li>&nbsp;git pull origin dev</li></ol><li>Create a new branch for this assignment (see Desired Branch Name)</li><ol><li>git checkout -b MP1-Tracker</li></ol><li>Create a new folder called MP1 in your local repository</li><li>Create a new file called tracker.py</li><li>Copy/paste the content from this template:&nbsp;&nbsp;<a href="https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da">https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da</a></li><li>Add/commit/push the template file</li><ol><li>git add --all</li><li>git commit -m "adding template"</li><li>git push origin MP1-Tracker</li></ol><li>Create a pull request from MP1-Tracker to dev (keep it open, do not close it until you're done)</li><li>Solve the various todo items (also noted below in the deliverables) and fill in the evidence</li><ol><li>Periodically add/commit; recommended after each solved item or every few items</li></ol><li>Save and copy/download the markdown</li><li>Create a new file mp1-submission.md in the MP1 folder</li><li>Add the markdown content</li><li>add/commit/push all the pending files for this assignment (tracker.py and mp1-submission.md)</li><li>If everything looks good on the pull request complete the merge</li><li>Create a new pull request from dev to prod and merge it to update prod (not used yet but you want to keep this up to date)</li><li>checkout dev locally and pull the changes to be up to date</li><li>Navigate to the prod branch on github and find the mp1-submission.md file and get the link to the file to submit to canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Add Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited add_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/220013342-9240a812-5d4d-4c39-a036-6a38c6b04f56.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code of sub_task 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/220013164-c326e8c6-7b50-45b3-a71f-8405cf5bcb9a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>output of sub_task 1<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of add_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/220013164-c326e8c6-7b50-45b3-a71f-8405cf5bcb9a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>output of sub_task 2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for add_task()</td></tr>
<tr><td> <em>Response:</em> <p>In this code, I have written the logic of adding the new task<br>and checking if the user is adding the info. in all the 3<br>fields or not. If not then displaying the empty fields to add and<br>the task wont be added. If the user enters all the 3 fields<br>properly following the instructions, then the task is added successfully.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Process Update Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited process_update() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/220202806-94e86977-a3c6-4ffa-a29c-6cbdac9ce713.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code of subtask<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/220202946-13fa0e20-c05d-4799-8815-ee62f8c36f6b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>output of the subtask with json file.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/220203536-318ed78a-cea0-4c9a-956b-0488d8b001a6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>index out of bound<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain the solutions to the checklist items for process_update()</td></tr>
<tr><td> <em>Response:</em> <p><span style="font-size: 13px;">get the task by index --&nbsp;</span><span style="background-color: rgb(30, 30, 30); font-family:<br>Consolas, &quot;Courier New&quot;, monospace; white-space: pre; color: rgb(156, 220, 254);">a</span><span style="background-color: rgb(30, 30,<br>30); color: rgb(212, 212, 212); font-family: Consolas, &quot;Courier New&quot;, monospace; white-space: pre;">=</span><span style="background-color:<br>rgb(30, 30, 30); font-family: Consolas, &quot;Courier New&quot;, monospace; white-space: pre; color: rgb(156, 220,<br>254);">tasks</span><span style="background-color: rgb(30, 30, 30); color: rgb(212, 212, 212); font-family: Consolas, &quot;Courier New&quot;,<br>monospace; white-space: pre;">[</span><span style="background-color: rgb(30, 30, 30); font-family: Consolas, &quot;Courier New&quot;, monospace; white-space:<br>pre; color: rgb(156, 220, 254);">index</span><span style="background-color: rgb(30, 30, 30); color: rgb(212, 212, 212);<br>font-family: Consolas, &quot;Courier New&quot;, monospace; white-space: pre;">][</span><span style="background-color: rgb(30, 30, 30); font-family: Consolas,<br>&quot;Courier New&quot;, monospace; white-space: pre; color: rgb(206, 145, 120);">&quot;name&quot;</span><span style="background-color: rgb(30, 30, 30);<br>color: rgb(212, 212, 212); font-family: Consolas, &quot;Courier New&quot;, monospace; white-space: pre;">]</span><div style="color: rgb(212,<br>212, 212); background-color: rgb(30, 30, 30); font-family: Consolas, &quot;Courier New&quot;, monospace; line-height: 19px;<br>white-space: pre;"><div>&nbsp; &nbsp; &nbsp; &nbsp; <span style="color: #9cdcfe;">b</span>=<span style="color: #9cdcfe;">tasks</span>[<span style="color: #9cdcfe;">index</span>][<span style="color:<br>#ce9178;">&quot;description&quot;</span>]</div><div>&nbsp; &nbsp; &nbsp; &nbsp; <span style="color: #9cdcfe;">c</span>=<span style="color: #9cdcfe;">tasks</span>[<span style="color: #9cdcfe;">index</span>][<span style="color: #ce9178;">&quot;due&quot;</span>]</div><div>In<br>this line I have taken task by index.<br></div><div>Index about of bound scenario is<br>handled in the if else condition. If index in range line is checking<br>the index out of bound scenario. If the input index is not in<br>the range </div><div>then else is called and printed index out of bound.</div><div>I have<br>passed variables a,b,c in the input</div><div>statement which display the already existing values for<br>that particular task.</div><div><br></div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Update Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited update_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/220209096-9b7c9f38-9873-41f6-aa8d-7e89e28e36ac.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code of update task <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/220209235-022527f0-01af-4d5c-a97a-837302bbb2c9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code part 2 of update task.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/220209514-fd8541af-ca68-459b-aefd-23f551621874.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of json file before updating the task index 4<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/220209679-1dcbf404-dc63-49a8-95dd-35093a2b9c99.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot after running update, we see that the task is updated.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of update_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/220209794-7c163498-0a4d-4e53-abe5-fc469499b433.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>task updated screenshot.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/220209933-e467e9a4-8a55-40c4-9a57-f9cc09960ed1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>task not updated screenshot as no changes provided.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for update_task()</td></tr>
<tr><td> <em>Response:</em> <p><span style="font-size: 13px;">find the task by index - The if condition which is<br>checking index in range is checking the&nbsp;</span><div><span style="font-size: 13px;">find the task by index-,the<br>update_task function is taking the input index as an argument in it and<br>that index is taken into if to check that the input input index<br>is out of bound or not. To check whether the task is updated<br>or not I have taken flags into consideration. If Flag is set 0<br>then the task is not updated(its printed at the end). If the flag<br>= 1 then the task is updated( if flag = 1 and if<br>the fields are non empty then the updated fields are going in the<br>variables.(its printed afterwards that the task is updated) Also the last activity is<br>updated as the task is also updated.</span><span style="font-size: 13px;"><br></span></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Mark Task Done/Complete Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited mark_done() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/220210786-814be88a-8d60-451c-a694-2df55b6f5f26.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code of the subtask<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of mark_done()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/220211119-3d6db2a3-36ca-4f48-9b54-92d6b6340ccc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>output of subtask <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for mark_done()</td></tr>
<tr><td> <em>Response:</em> <p>The function is checking the out of bound through the if condition index<br>in range. The main logic checks that the json file. If the json<br>file has false for done then as the user wants to complete then<br>the date time is updated and the task is completed. else the task<br>is already completed as it must be having some date in the front<br>of done.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> View Task Logic (and list) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited view_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/220213327-ead0e3f4-fd72-42c0-891e-a33eea5d1b05.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code screenshot.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of view_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/220213030-eac058b2-d8df-4522-9c42-97ec58994a97.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2 index out of bound<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/220213105-2099e39c-ccba-44e9-8030-50f3bceba7a3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>output of subtask<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot(s) of list_tasks() output showing a few examples</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/220213105-2099e39c-ccba-44e9-8030-50f3bceba7a3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here we are viewing the task which is already there in the json<br>file. Hence every field in the task index is getting stored in the<br>same name variable and printing the output in the print statement already given.<br><br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/220213270-9801fe28-6a80-4a90-8ce8-2ae003ad3397.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>output of the task.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited delete_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/220221379-3d3c7175-4c67-41df-8d8b-328af1a8f469.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for the subtask.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of delete_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/220221465-0afad463-75a6-4a0a-98f8-3fccd9643ec2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before deletion json file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/220221553-4eb44a0f-85a7-4321-8a09-f592d9122bb2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>output of the subtask<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for delete_task()</td></tr>
<tr><td> <em>Response:</em> <p>The if condition which is taking index in range len(tasks) is checking the<br>array out of bound scenario. The actual logic is just in the word<br>del. The del word is deleting the record from the json file. I<br>am just passing the dictionary with the index through del word to delete<br>the record.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Get Incomplete Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_incomplete_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/220223656-b75eb8e9-8af2-431e-8910-73056347d3ae.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code screenshot of the subtask<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_incomplete_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/220223765-acc1a26c-3567-42a5-bb9c-51589b998e77.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output screenshot, which gives output of all incomplete tasks.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/220224025-c6421e0c-3e2f-49b2-a029-7939db1d7373.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here I done( completed 1 task) and checked that it should not come<br>in incomplete list.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_incomplete_tasks()</td></tr>
<tr><td> <em>Response:</em> <p>Here, we are considering the whole list, and finding out the incomplete tasks.<br>here I have checked the whole list and found the tasks in the<br>list where the Done field has false to it. If there is false<br>along done that means the task is incomplete. Hence, I am appending all<br>those tasks in a list called _tasks and then passing it into the<br>already coded function named&nbsp;<span style="color: rgb(220, 220, 170); background-color: rgb(30, 30, 30); font-family:<br>Consolas, &quot;Courier New&quot;, monospace; white-space: pre;">list_tasks</span><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Get Over Due Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_overdue_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/220224937-d44b4186-fba0-498c-a973-a88e591cf573.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code of the subtask<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_overdue_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/220225089-b1d4dd9a-4c53-4e61-a4dc-547f463ad063.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>output showing 1 overdue task<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/220225263-82db6058-6c1d-407a-9415-144cfa0f1582.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>as now there is no overdue task, it says no tasks to show<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_overdue_tasks()</td></tr>
<tr><td> <em>Response:</em> <p>Here, we are considering the whole list, and finding out the overdue tasks.<div>In<br>this simple line of code:</div><div>if (str_to_datetime(str(tasks[i][&quot;due&quot;])) &lt; datetime.now() and tasks[i][&quot;done&quot;] == False):<br></div><div>I have<br>checked, the due date in the json file for the tasks added has<br>already been passed the current date or not. AND the done should have<br>the False value too.&nbsp;</div><div>That means the task is overdue.Then I am appending that<br>overdue list in_tasks and then passing it into the already coded function named&nbsp;&lt;span<br>style=&quot;color: rgb(220, 220, 170); background-color: rgb(30, 30, 30); font-family: Consolas, &quot;Courier New&quot;, monospace;<br>white-space: pre;&quot;&gt;list_tasks</span></div><div><br></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Get Time Remaining Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_time_remaining() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/220228348-2713a617-651c-4743-907c-4363a7873b0f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code of the subtask<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_time_remaining()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/220228604-99c68a9c-4dcc-41a8-95c1-f4508dec447b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output screenshot of the subtask.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_time_remaining()</td></tr>
<tr><td> <em>Response:</em> <p>Here, through if condition I am checking the index in range as usual.<div>Then,<br>these lines in code:</div><div><div>if(datetime.now() &lt; str_to_datetime(str(tasks[index][&quot;due&quot;]))):</div><div>print(&quot; Your task is due by&quot;,str_to_datetime(str(tasks[index][&quot;due&quot;]))- datetime.now())</div></div><div>compares todays<br>date is less than the date in the task, If yes, then the<br>task is due by the subtraction of both the string format dates giving<br>us the no of days the task is due by.</div><div>Then, these lines in<br>code:<br></div><div><div>elif(datetime.now() &gt; str_to_datetime(str(tasks[index][&quot;due&quot;]))):</div><div>print(&quot;Your task is overdue by&quot;,datetime.now() - str_to_datetime(str(tasks[index][&quot;due&quot;])))</div></div><div>compares todays date is greater<br>than the date in the task, If yes, then the task is overdue<br>by the subtraction of both the string format dates giving us the no<br>of days the task is overdue by.<br></div><div><br></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of program output generated from filling in this deliverable (or close to it)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/220230265-56932731-1768-4ba2-8333-14079ed33b60.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>output of add/update/view<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/220230555-d563f6e9-9f74-40e4-b1b0-c78d79315630.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of done/list/incomplete<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/220230717-dc33ff97-d148-4258-be94-73da6868bbac.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of overdue/delete/remaining<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) of the saved JSON file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/220230891-e0e2e2a5-edc5-4daf-9aea-38ff2c4f1964.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot attached as mentioned.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Discuss any issues and how they were overcome or learnings from this project</td></tr>
<tr><td> <em>Response:</em> <ol><br><li>learnt the use of lists.<div>2. learnt the use of dictionaries.</div><div>3. Learnt functions<br>like str_to_datetime(), datetime.now()</div><div>4. Basic logic building.</div><div>5. use of functions/ loops/ if else conditions<br>etc.</div><br></li><br></ol><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request for this assignment (project branch to dev)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rk268/IS601/pull/8">https://github.com/rk268/IS601/pull/8</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-1-tracker-app/grade/rk268" target="_blank">Grading</a></td></tr></table>