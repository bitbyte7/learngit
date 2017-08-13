#!/usr/bin/env python
# -*- coding: utf-8 -*-

#This code show how blockchain works
import hashlib as hasher
import datetime as date

#Define a virture coin named snakecoin
class Block:
	def __init__(self, index, timestamp, data, previours_hash):
		self.index = index
		self.timestamp = timestamp
		self.data = data
		self.previours_hash = previours_hash
		self.hash = self.hash_block()
	def hash_block(self):
		sha = hasher.sha256()
		sha.update(str(self.index).encode('utf-8') + str(self.timestamp).encode('utf-8') + str(self.data).encode('utf-8') + str(self.previours_hash).encode('utf-8'))
		return sha.hexdigest()

#Generate gensis block
def creat_genesis_block():
	return Block(0, date.datetime.now(), "Genesis Block", "0")
	#Manually construct a block with index zero and aritraty previous hash

#Generate all later blocks in the blockchain
def next_block(last_block):
	this_index = last_block.index + 1
	this_timestamp = date.datetime.now()
	this_data = "Hey, I am a block." + str(this_index)
	this_hash = last_block.hash
	return Block(this_index, this_timestamp, this_data, this_hash)

#Create the blockchain and add the genesis block
blockchain = [creat_genesis_block()]
previous_block = blockchain[0]

#How many blocks should we add to the chain after the genesis block
num_of_blocks_to_add = 20

for i in range(0, num_of_blocks_to_add):
	block_to_add = next_block(previous_block)
	blockchain.append(block_to_add)
	previous_block = block_to_add

#Tell everyone about this blockchain
print("Block #{} has been added to the blockchain!".format(block_to_add.index))
print("Hash: {}\n".format(block_to_add.hash))