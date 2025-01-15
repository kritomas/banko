-- Banqo: Copyright (C) 2025 kritomas, kritomasx@gmail.com
-- If using MariaDB, he database has to be created with the utf8mb4 character set and utf8mb4_bin collation:
-- create database banqo character set = 'utf8mb4' collate = 'utf8mb4_bin';

start transaction;

create table Address
(
	id int primary key auto_increment,
	city varchar(64) not null,
	street varchar(64) not null,
	house_number varchar(4) not null,
	additional varchar(128)
);
create table Client
(
	id int primary key auto_increment,
	Address_id int not null,
	first_name varchar(32) not null,
	last_name varchar(32) not null,
	email varchar(256) unique not null,
	client_number varchar(32) unique not null,

	foreign key (Address_id) references Address(id)
);
create table Bank
(
	id int primary key auto_increment,
	Address_id int not null,
	bank_number varchar(32) unique not null,

	foreign key (Address_id) references Address(id)
);
create table Account
(
	id int primary key auto_increment,
	Client_id int not null,
	Bank_id int not null,
	account_type enum('basic', 'savings') not null,
	account_number varchar(32) unique not null,
	is_frozen bit not null default 0,
	created_on datetime not null default current_timestamp,
	balance decimal(16, 2) not null default 0 check(balance >= 0),

	foreign key (Client_id) references Client(id),
	foreign key (Bank_id) references Bank(id)
);
create table Transaction
(
	id int primary key auto_increment,
	from_id int not null,
	to_id int not null,
	created_on datetime not null default current_timestamp,
	amount decimal(16, 2) not null default 0 check(amount >= 0),
	notes varchar(512),

	foreign key (from_id) references Account(id) on delete cascade,
	foreign key (to_id) references Account(id) on delete cascade
);

create view Client_Accounts as
select first_name, last_name, email, client_number, account_number, account_type, is_frozen, created_on, balance from Client join Account on Client_id=Client.id;

create view Transactions as
select from_acc.account_number as from_account, to_acc.account_number as to_account, Transaction.amount, Transaction.created_on as took_place_on, Transaction.notes as notes
from Transaction join Account from_acc on Transaction.from_id = from_acc.id join Account to_acc on Transaction.to_id = to_acc.id;

delimiter //
create procedure Bank_Transfer(in from_account_number varchar(32), in to_account_number varchar(32), in amount decimal(16, 2), in notes varchar(512))
begin
	declare from_id int default null;
	declare to_id int default null;

	start transaction;
	update Account set balance = balance - amount where account_number = from_account_number;
	update Account set balance = balance + amount where account_number = to_account_number;

	select id into from_id from Account where account_number = from_account_number;
	select id into to_id from Account where account_number = to_account_number;
	insert into Transaction (from_id, to_id, amount, notes) values (from_id, to_id, amount, notes);
	commit;
end //
create procedure Bank_Transfer_Without_Notes(in from_account_number varchar(32), in to_account_number varchar(32), in amount decimal(16, 2))
begin
	call Bank_Transfer(from_account_number, to_account_number, amount, null);
end //
delimiter ;

commit;

-- Required grants: SELECT,INSERT,UPDATE,DELETE,EXECUTE