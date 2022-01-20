import sqlite3
from data import Contract, Transaction


connection = sqlite3.connect(
    ":memory:"
)  # instead of :memory: use DbName.db in production

cursor = connection.cursor()

createContractTable_command = """CREATE TABLE contracts(
                address text,
                standard text,
                chain text
                );"""

cursor.execute(createContractTable_command)
connection.commit()


def handleNewContract(contract):
    with connection:
        cursor.execute(
            "INSERT INTO contracts VALUES (?,?,?)",
            (contract.address, contract.standard, contract.chain),
        )

        cursor.execute(
            "CREATE TABLE '{}'(address text,tokenAmount real,usdValue real,transactionType text);".format(
                contract.address
            )
        )


def addNewTransaction(transaction):
    with connection:
        cursor.execute(
            "INSERT INTO '{}' VALUES (?,?,?,?)".format(transaction.address),
            (
                transaction.address,
                transaction.tokenAmount,
                transaction.usdValue,
                transaction.transactionType,
            ),
        )


def getTransactionDetails(contractAddress):
    cursor.execute(
        "SELECT * FROM contracts INNER JOIN '{}' using(address)".format(contractAddress)
    )


def setVars():
    contract = Contract("This is a address", "ERC721", "Polygon")
    transaction = Transaction("This is a address", 20.000001, 45.45, "buy")
    return contract, transaction


def execute(contract, transaction):
    handleNewContract(contract)
    addNewTransaction(transaction)
    getTransactionDetails(contract.address)


def main():
    contract, transaction = setVars()
    execute(contract, transaction)


main()
print(cursor.fetchall())

connection.close()
