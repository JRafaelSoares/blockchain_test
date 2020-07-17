import unittest
from blockchain.blockchain_data_structure import Blockchain, Transaction
from crypto.keygen import generate_key_pair

# --------------------------------------- #
# ----------- Variable Values ----------- #
# --------------------------------------- #

miner_address = "catarina-address"
node_identifier = "test"
host = '0.0.0.0'
port = 5000
blockchain_address = '{}:{}'.format(host, port)
from_address = "from_address"
to_address = "to_address"
amount = 1.0


class TestBlockchainClass(unittest.TestCase):

    generate_key_pair(node_identifier)

    # ------------------------------------- #
    # --------- Constructor Tests --------- #
    # ------------------------------------- #

    def test_constructor_correct(self):
        blockchain = Blockchain(miner_address, node_identifier, host, port)
        self.assertEqual(blockchain.miner_address, miner_address)
        self.assertEqual(blockchain.node_identifier, node_identifier)
        self.assertEqual(blockchain.address, blockchain_address)

    def test_constructor_null_miner_address(self):
        with self.assertRaises(Exception):
            Blockchain(None, node_identifier, host, port)

    def test_constructor_null_node_identifier(self):
        with self.assertRaises(Exception):
            Blockchain(miner_address, None, host, port)

    def test_constructor_null_host(self):
        with self.assertRaises(Exception):
            Blockchain(miner_address, node_identifier, None, port)

    def test_constructor_null_port(self):
        with self.assertRaises(Exception):
            Blockchain(miner_address, node_identifier, host, None)

    # ------------------------------------- #
    # ---------- Gen Block Tests ---------- #
    # ------------------------------------- #

    def test_gen_block_correct(self):
        gen_block = Blockchain(miner_address, node_identifier, host, port).calculate_gen_block()
        self.assertEqual(gen_block.index, 0)
        self.assertEqual(gen_block.previousHash, "0")
        transaction = gen_block.transactions
        self.assertTrue(isinstance(transaction, Transaction))
        self.assertEqual(transaction.amount, 0.0)
        self.assertEqual(transaction.fromAddress, None)
        self.assertEqual(transaction.toAddress, " ")
        self.assertEqual(transaction.node_id, node_identifier)

    # ------------------------------------- #
    # ----- Create Transaction Tests ------ #
    # ------------------------------------- #

    def test_create_transaction(self):
        blockchain = Blockchain(miner_address, node_identifier, host, port)
        transaction = blockchain.create_transaction(from_address, to_address, amount)
        self.assertEqual(transaction.fromAddress, from_address)
        self.assertEqual(transaction.toAddress, to_address)
        self.assertEqual(transaction.amount, amount)
        self.assertEqual(len(blockchain.pending_transactions), 1)
        self.assertEqual(blockchain.pending_transactions[0], transaction)

    def test_create_transaction_no_from_address(self):
        with self.assertRaises(Exception):
            Blockchain(miner_address, node_identifier, host, port)\
                .create_transaction(None, to_address, amount)

    def test_create_transaction_no_to_address(self):
        with self.assertRaises(Exception):
            Blockchain(miner_address, node_identifier, host, port)\
                .create_transaction(from_address, None, amount)

    def test_create_transaction_no_amount(self):
        with self.assertRaises(Exception):
            Blockchain(miner_address, node_identifier, host, port)\
                .create_transaction(from_address, to_address, None)

    # ------------------------------------- #
    # ------- Block Creation Tests -------- #
    # ------------------------------------- #

    def test_block_creation_(self):
        blockchain = Blockchain(miner_address, node_identifier, host, port)
        transaction_list = []
        for transactions in range(blockchain.number_of_transactions):
            transaction_list.append(blockchain.create_transaction(from_address, to_address, amount))

        self.assertEqual(len(blockchain.chain), 2)
        new_block = blockchain.chain[1]
        previous_block = blockchain.chain[0]
        self.assertEqual(new_block.index, previous_block.index+1)
        self.assertEqual(new_block.previousHash, previous_block.currentHash)
        self.assertEqual(new_block.transactions, transaction_list)

    def test_block_creation_reward_transaction(self):
        blockchain = Blockchain(miner_address, node_identifier, host, port)

        for transactions in range(blockchain.number_of_transactions):
            blockchain.create_transaction(from_address, to_address, amount)

        self.assertEqual(len(blockchain.pending_transactions), 1)
        transaction = blockchain.pending_transactions[0]
        self.assertEqual(transaction.toAddress, blockchain.miner_address)
        self.assertEqual(transaction.fromAddress, None)
        self.assertEqual(transaction.amount, blockchain.miningReward)

    # ------------------------------------- #
    # ----------- Balance Tests ----------- #
    # ------------------------------------- #



if __name__ == '__main__':
    unittest.main()