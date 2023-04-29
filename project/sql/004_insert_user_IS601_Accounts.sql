INSERT IGNORE INTO
    IS601_Users (
        id,
        email, 
        username, 
        password
    )
VALUES (-1,'system_user_rk268@gmail.com', 'rk268_system_user', '$4c$12$wRt2/iPKMDy3XQ1rDL1eg.8bnl5AG3KD2jWOW48Qnsb/oAYHG/xHC');
INSERT INTO
    IS601_Accounts (
        id,
        account_number, 
        account_type, 
        user_id
    )
VALUES (-1,'000000000000','World',-1);

