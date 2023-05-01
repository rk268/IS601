<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Bank Project</td></tr>
<tr><td> <em>Student: </em> Rupak Avinash Kulkarni (rk268)</td></tr>
<tr><td> <em>Generated: </em> 4/30/2023 10:04:43 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-2-bank-project/grade/rk268" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Create Accounts table and setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot from the db of the system user (Users table)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235318305-9d5b7f68-a8c1-4f67-a19e-fb13fd06356b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>id with -1 is the system user <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot from the db of the world account (Accounts table)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235318337-4d1a747b-19b7-4ba8-b376-81c9f0460634.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>As per the screenshot, the id = -1 user_id = -1 has the<br>required data.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain the purpose and usage of these two entries and how they relate</td></tr>
<tr><td> <em>Response:</em> <p>We require users to have accounts in order to conduct any transactions. Users<br>with accounts are required for all transactions, including withdrawals, deposits, transfers, and other<br>operations since the foreign key user_id in the accounts database identifies the user<br>to whom the account belongs. Additionally, the foreign keys src and dest in<br>the Transactions table refer to the accounts table&#39;s unique account id. Thus, the<br>aforementioned entries are required in order to complete the transaction.&nbsp; &nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rk268/IS601/pull/32">https://github.com/rk268/IS601/pull/32</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Dashboard </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the requested links/navigation</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235383098-b888fdd3-b903-472f-a643-2440d85143f1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>drop-down visible with all necessary options.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235383156-c74de7e6-7cb5-4b6c-a1dc-2680ea759e2f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Create account visible<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235383185-91f4e1fa-d7bf-46a5-b0cd-bd86bd54fea3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>dropdown options.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain which ones are working for this milestone</td></tr>
<tr><td> <em>Response:</em> <p>made changes in nav.html by adding the necessary links.&nbsp;<br>As of now, created create<br>route and redirected it to its from only. Also created the actual dropdown<br>in the forms.py and the account_form.html has the total html.<br>Createform has the variable<br>form passed in accounts.py<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rk268/IS601/pull/33">https://github.com/rk268/IS601/pull/33</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Create a checking Account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the Create Account Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235389108-9674480e-4e67-4e0e-9ff5-c2dc306a2468.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of valid data filled in.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots showing validation errors and success message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235383270-376b8796-2747-4e58-8f35-1fdf73f1e64a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Minimum funding should be 5. Hence when entered less than 1 we see<br>a message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235383334-b13f657c-f7e3-4286-b9c1-572a6c04c401.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Attempting to create a new checking account.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235383369-a6bfb89d-0e7b-4275-a563-4bc950546e3a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Account created successfully message visible<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot showing the transaction generated from the initial deposit (from the DB)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235383464-68734e38-7185-4af1-b3b2-35e856ed4019.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>-ve and +ve values entry values are properly visible in the transactions table.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain which account number generation you used and the account creation process including the transaction logic</td></tr>
<tr><td> <em>Response:</em> <p>In this, the id which is getting through form is passed to IS601_Accounts<br>and that is mapped to transactions table. In transactions table, the entered amount<br>is subtracted from its balance and added to that particular user balance. Also<br>1 user can have various types of multiple accounts.&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rk268/IS601/pull/34">https://github.com/rk268/IS601/pull/34</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-rk268-dev.herokuapp.com/accounts/create">https://is601-rk268-dev.herokuapp.com/accounts/create</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> User will be able to list their accounts </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the user's account list view (show 5 accounts)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235383642-865dc21b-4950-4224-b6d4-6a8a02beedc9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot has 5 entries with all the fields needed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the page is displayed and the data lookup occurs</td></tr>
<tr><td> <em>Response:</em> <p>It is basic select query. When we get the user id from the<br>form. We just select that and display the all the records for that<br>that select. Also adding transactions button for future deliverable.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rk268/IS601/pull/37">https://github.com/rk268/IS601/pull/37</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-rk268-prod.herokuapp.com/accounts/list">https://is601-rk268-prod.herokuapp.com/accounts/list</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Account Transaction Details </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of an account's transaction history</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235383682-d8a7e7db-3429-4bae-8647-af01f72f96c3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>sample1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235383717-4510b8fd-08dc-4fa2-8eea-f0b90edb72eb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sample2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235383744-033537b5-e794-49f0-bdd4-85b211f047cb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sample3<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the lookup and display occurs</td></tr>
<tr><td> <em>Response:</em> <p>Here, we see the transactions. The db first db query which is select<br>from accounts is fetching the account number on which we have selected, then<br>the account number is passed to the other query which is select from<br>transaction.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rk268/IS601/pull/39">https://github.com/rk268/IS601/pull/39</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-rk268-prod.herokuapp.com/accounts/transactions?acc_number=000000000002">https://is601-rk268-prod.herokuapp.com/accounts/transactions?acc_number=000000000002</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Deposit/Withdraw </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a Screenshot of the Deposit Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235383782-a7ac37e0-2a55-4d28-8655-92a5cc5c826c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot displays that I am selecting the deposit option from the drop<br>down.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235384614-7a8a81e7-8bc7-4ea7-9723-73a0e6956241.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Depositing  $40 for checking 000000000003 with Memo<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235384728-33ec012b-5f45-4f30-a719-fc81524fb33e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successfully deposited $40.0 flash message displayed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a Screenshot of the Withdraw Page (this potentially can be the same page with different views)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235386223-bf8cc117-38c4-46d4-8aa0-50cd14b422de.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Selecting withdraw option from the drop down<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235386536-f1f5a309-4e52-4424-9cbb-f7f6a3c7fc34.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Selecting the desired checking account number.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235386605-4c995a4b-1c2e-416d-90a2-5690e9d86f31.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Adding the funds with the memo to withdraw amount.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235386645-97879e94-2386-4998-bb5e-844186ca8e19.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successfully withdrew $10.0 flash message visible. <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show validation error for negative numbers</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235387037-eb47a078-e1bd-422b-907a-70759d7b7eef.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>For deposit option, It does not accept negative value and shows appropriate error<br>message.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235387121-5787d492-9cdb-4a00-a3c6-f6c31fe87faa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>For withdraw option also, It does not accept negative value and shows appropriate<br>error message.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Show validation error for withdrawing more than the account contains</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235387198-97d6d937-d109-44f4-a7ee-cfd02a5a357e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The checking account has $60. Now I will try withdrawing $1000 from it.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235388849-b2a4f857-8a8c-4eac-866c-151240ffd2d9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>flash message displaying cant withdraw the amount greater than your balance!!<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Show a success message for deposit and withdraw (2 screenshots)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235384728-33ec012b-5f45-4f30-a719-fc81524fb33e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Deposit success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235386645-97879e94-2386-4998-bb5e-844186ca8e19.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Withdraw success message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Show a screenshot of the transaction pairs in the DB for the above tests</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235384919-473400ba-b97a-4b3a-8104-156cf1f64cbe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Please check the tick marks in the first DB table coloumn. As you<br>can see account src is 3. Its expected total is 30 (which is<br>amount he/she has in its account. Now 40 dollars are  deposited(check last<br>tickmark) We can see that the expected total is 70 for that account<br>as we deposited 40 in it. Hence total 40 dollars are subtracted from<br>the world bank.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235386795-33065da3-d926-4039-9c81-f75008d59fd6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Please check the highlighted part which has tick marks. We see that the<br>users old expected total was $70. Now I withdrew $10 dollars from its<br>checking account. Hence, now the expected balance is $60 and there is +$10<br>in the world bank. Initially world bank had $999999519. But now it has<br>$999999529.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Briefly explain how transactions work</td></tr>
<tr><td> <em>Response:</em> <div>The first query is used to update the balance in the accounts table<br>when a deposit or withdrawal is made, while the second query creates a<br>new record in the transactions table. The src and dest are identical to<br>the account id of that account for deposits and withdrawals.&nbsp;</div><div>When making a deposit,<br>the difference value is entered with a positive sign; when making a withdrawal,<br>it is entered with a negative sign.&nbsp; Positive sign means when deposited goes<br>in the users account. and negative sign is subtracted from the world bank<br>and vice versa for the withdraw. For withdraw, the expected balance is checked<br>and if the amount&nbsp; entered by the user for that account is greater<br>than the value is DB then the respective flash message is written.&nbsp; In<br>the deposit route, the first DB query fetches the account id which is<br>then appended in the next query in transaction table.&nbsp;</div><br></td></tr>
<tr><td> <em>Sub-Task 8: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rk268/IS601/pull/42">https://github.com/rk268/IS601/pull/42</a> </td></tr>
<tr><td> <em>Sub-Task 9: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-rk268-prod.herokuapp.com/accounts/deposit">https://is601-rk268-prod.herokuapp.com/accounts/deposit</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <div>Working on the deposit and withdraw and balance initially took time, as the<br>concept of world bank and the transactions concept were bit critical. But once<br>the logic was ready, it helped for other cases too.</div><div>1) I learned about<br>sending data between pages using session data or arguments.</div><div>2) Also, learnt 1 new<br>thing, that its no need to create or do HTML for a column<br>which is there in HTML. I added Memo column without its html in<br>the transactions page.</div><div>3) I acquired new knowledge adding input field validations using WTF<br>forms and backing validation.</div><div>4) Acquired the ability to apply SQL queries to a<br>problem statement.</div><div><br></div><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-rk268-prod.herokuapp.com/login">https://is601-rk268-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-2-bank-project/grade/rk268" target="_blank">Grading</a></td></tr></table>