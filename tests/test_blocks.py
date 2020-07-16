import unittest
from datetime import datetime
from blockchain.blockchain_data_structure import Block
from blockchain.blockchain_data_structure import Transaction
from crypto.keygen import generate_key_pair

# --------------------------------------- #
# ----------- Variable Values ----------- #
# --------------------------------------- #

node_identifier = "test"
from_address = "from_address"
to_address = "to_address"
amount = 1
transaction = Transaction(from_address, to_address, amount, node_identifier)

class TestBlockClass(unittest.TestCase):

    generate_key_pair(node_identifier)

    # ------------------------------------- #
    # --------- Constructor Tests --------- #
    # ------------------------------------- #

    def test_constructor_correct(self):
        timestamp = datetime.now
        block = Block(timestamp, transaction, 0)
        self.assertEqual(block.timestamp, timestamp)
        self.assertEqual(block.transactions, transaction)
        self.assertEqual(block.index, 0)

    # TODO - Add test for wrong type timestamp
    def test_constructor_null_timestamp(self):
        with self.assertRaises(Exception):
            Block(None, transaction, 0)

    def test_constructor_null_transaction(self):
        with self.assertRaises(Exception):
            Block(datetime.now(), None, 0)

    def test_constructor_null_transaction_list(self):
        with self.assertRaises(Exception):
            Block(datetime.now(), [None], 0)

    def test_constructor_transaction_list_with_null(self):
        with self.assertRaises(Exception):
            Block(datetime.now(), [transaction, None], 0)

    # ------------------------------------ #
    # ----------- Aux Function ----------- #
    # ------------------------------------ #

    # Returns a correctly made and signed transaction
    def get_correct_transaction(self):
        return Transaction(from_address, to_address, amount, node_identifier)


if __name__ == '__main__':
    unittest.main()