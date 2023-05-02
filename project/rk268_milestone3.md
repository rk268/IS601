<table><tr><td> <em>Assignment: </em> IS601 Milestone 3 Bank Project</td></tr>
<tr><td> <em>Student: </em> Rupak Avinash Kulkarni (rk268)</td></tr>
<tr><td> <em>Generated: </em> 5/2/2023 7:40:47 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-3-bank-project/grade/rk268" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone3 branch</li><li>Create a new markdown file called milestone3.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone3.md</li><li>Add/commit/push the changes to Milestone3</li><li>PR Milestone3 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 4</li><li>Submit the direct link to this new milestone3.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on GitHub and everywhere else. Images are only accepted from dev or prod, not localhost. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> User will be able to transfer between their accounts </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of transfer page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235545122-8d9b977d-800a-4f83-94e4-82949ed2f484.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the internal Transfer heading from heroku dev URL.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot showing dropdown values</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235545122-8d9b977d-800a-4f83-94e4-82949ed2f484.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the account number as well as the current account balance.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot showing user can't transfer more funds than they have</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235545473-88c3e0e1-3c0d-4c4f-a102-2968af8d0137.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Amount you are trying to transfer is exceeding the balance amount message flashing.<br>Here account 002 has $70 and I am trying to transfer $100.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshot showing user can't transfer to the same account</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235545725-e60a0baf-8c9a-4d79-81e2-b086052584c3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Transfer between 2 same accounts is not expected/allowed message flashing as I am<br>trying to transfer from 002 to 002 accounts.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235545941-e9075742-6548-4d2d-863f-3b7f7aa8bbe3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Transfer between 2 same accounts code snippet.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshot showing you can't transfer an negative balance</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235546141-13f495fc-493f-46bd-8952-14df47e5bf5f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Number must be at least 1. message as I am trying to transfer<br>-ve account.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235547027-7c0dac59-b235-49e5-93fd-7adc6c7b2dfc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Number must be at least 1. code snippet.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshot of the generated transaction history from the db</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235547377-0a81cc90-924b-4882-85e5-ae2666a487d7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot highlights the db transfer history.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a screenshot of the Accounts table showing both affected accounts</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235547973-d3ed5dec-6f42-4d88-af05-66137601aa45.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Transferred $10.0 from account number 6 to 4 for refrence<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235548067-8be571e0-08dc-4166-8a63-74801a040b1b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>As you can see the balance in the db accounts table acc 6<br>balance was 60 before is now 50 and acc 4 balance was initially<br>0 and now its 10.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Briefly explain the code process/flow of a transfer including how the accounts are fetched for the dropdowns</td></tr>
<tr><td> <em>Response:</em> <ol><br><li>A select query (user_id is retrieved from session data) retrieves all accounts<br>for the currently logged-in user. The select query&#39;s list of accounts is sent<br>to the jinja template for the transfer money page, where the list is<br>iterated several times to create dropdown menus.<div><div>2) For each source account and destination<br>account, a single select query retrieves the corresponding balances. A suitable error message<br>is displayed to the user if the source balance is less than the<br>amount to transfer or when transferring to an unsupported account or the same<br>account.</div><div>3) One update query subtracts money from the balance of the source account,<br>while another update query adds money to the balance of the destination account.</div><div>A<br>new record is added to the transactions table, containing the source and destination<br>account numbers, the amount transferred, and other information, following the successful completion of<br>both queries.</div><div><br></div></div><br></li><br></ol><br></td></tr>
<tr><td> <em>Sub-Task 9: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rk268/IS601/pull/49">https://github.com/rk268/IS601/pull/49</a> </td></tr>
<tr><td> <em>Sub-Task 10: </em> Add link to transfer page from heroku</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-rk268-prod.herokuapp.com/accounts/transfer">https://is601-rk268-prod.herokuapp.com/accounts/transfer</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Transaction History Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of transaction history page showing the new transfer transaction</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235550057-b93e8fb6-4c71-4ddb-acff-20168df53d7b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Please check memo rupak k . It has the transaction type as transfer.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots demonstrating the filters and pagination</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235552125-f83944a7-f23e-4352-a8f1-98d2417daa6b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>filter deposit added.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235552220-9114e1ef-b107-467b-b172-eef3b1614a86.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>filter withdraw applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235552312-fd84ad96-8aaa-4908-8232-18dfdbb19f60.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>filter transfer applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235552413-2f798e26-dd26-4076-ae77-92f09b110985.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>pagination seen( page 1)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235552494-916c1fcb-27ee-4dae-9645-dedf3fe2b31f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>pagination seen( page 2)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how the filters/pagination work</td></tr>
<tr><td> <em>Response:</em> <div>As in the transactions code, pagination is used. When the page is re-rendered,<br>it uses the number of rows stated and displays that many rows because<br>I set items_per_page to 10 and supplied it to the rows variables. Additionally,<br>I've declared a variable called "transaction type" for filtering, and I passed it<br>the input from the request.args file. As soon as it receives the argument,<br>it searches the table and displays the data with those filters.</div><div><br></div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rk268/IS601/pull/51">https://github.com/rk268/IS601/pull/51</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add link to Transaction History page from heroku</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-rk268-prod.herokuapp.com/accounts/transactions?acc_number=000000000003">https://is601-rk268-prod.herokuapp.com/accounts/transactions?acc_number=000000000003</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> User's profile First name and Last name </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the user's profile with the new fields</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235592617-0eef333d-13f4-4b27-ac12-05d24a8bd936.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Login username and password through which I am logging in.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235593143-e0c9d8a2-3a18-44b9-9a23-cff520a9cabd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB screenshot for that login<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235593257-f4e25259-cfd6-4347-8a06-9503fbe82379.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Already prefilled FIRSTNAME and LASTNAME  in the profile field.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rk268/IS601/pull/53">https://github.com/rk268/IS601/pull/53</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Add link to profile page from heroku</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-rk268-prod.herokuapp.com/profile">https://is601-rk268-prod.herokuapp.com/profile</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> User will be able to transfer funds to another user </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the external transfer page with filled in data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235775213-8ce3feeb-5e51-42c2-9c6f-6b878abb8258.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>External transfer heading visible.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot showing user can't send more than they have</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235775602-d15e466b-2849-40ee-8789-7050f0675a79.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Amount you are trying to transfer is exceeding the balance flash message flashed.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235776018-0c456874-bc03-46c4-bed4-a1d7d384bf3e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code checking the balance in the if condition and passing it to the<br>function and checking if its negative then the answer is negative which is<br>less than 0 making the if condition true. Hence the flash error message<br>is flashed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot showing they can't send a negative amount</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235776443-3f925490-eab3-4261-93a1-d36326374d60.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Proper error message is flashed which says Number must be at least 1.<br>and the query isn&#39;t triggered.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235777120-5908c433-29ce-472b-a5ef-e2695cfd4f00.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>In the forms.py , the number range is set to min1. Hence, funds<br>cant be negative.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshot(s) showing message if a user doesn't exist and/or a destination account wasn't found</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235778087-1ff69176-0112-4fc2-b473-7e1e339d4a60.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>account not found in the database flashed if entered information is not in<br>the database.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235806084-d9518d02-1b96-4c77-b325-8d09684a58cc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>account not found in the database flashed if entered information is not in<br>the database- Here the account number entered is invalid<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235806430-0d0001f3-a67e-40ae-aa6b-38eb0cf7a562.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The dest_user variable is checking the form entered value with the ID in<br>the IS601_users table if it doesnt find that then it goes into except<br>block and the account not found in database message is flashed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshot of the transactions table showing the recorded transfer</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235805618-47bb09cb-e9c3-4d53-8f8c-83e493a03340.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The tick mark accounts are the accounts which are needed to take under<br>consideration. The 002($105) is source and 0014($245) is the destination account. Now I<br>will show the EXT_TRANSFER<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235805747-cde0052a-fd20-4253-a3eb-7aa1472ac998.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>UI Message Screenshot<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235805857-9a1a9c93-aa27-4a74-b77e-2745ca7bc7bb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Check the ticked entries . EXT_Transfer is done successfully.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshot(s) showing the updated account balances</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113077/235805857-9a1a9c93-aa27-4a74-b77e-2745ca7bc7bb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Check the ticked entries . EXT_Transfer is done successfully.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Briefly explain the process of looking up the target user's account and the validation logic</td></tr>
<tr><td> <em>Response:</em> <p>The select query executes which searches for destination account id. If the id/name<br>is found, then the money is transferred else an error message is thrown.&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 8: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rk268/IS601/pull/56">https://github.com/rk268/IS601/pull/56</a> </td></tr>
<tr><td> <em>Sub-Task 9: </em> Add link to external transfer page from heroku</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-rk268-prod.herokuapp.com/accounts/ext_transfer">https://is601-rk268-prod.herokuapp.com/accounts/ext_transfer</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <div>1) I learned how to transmit data from one page to another using<br>session data or arguments.</div><div>2) I gained knowledge by adding validations to WTF forms<br>and using backed validation for input fields.</div><div>3) Acquired knowledge on how to use<br>SQL queries to solve a problem.</div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-3-bank-project/grade/rk268" target="_blank">Grading</a></td></tr></table>