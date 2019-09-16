import unittest
from airflow.models import DagBag



class TestAllDagValidation(unittest.TestCase):
    def test_import_dags(self):
        dagbag = DagBag(dag_folder='../dags/',include_examples=False)
        for dag_id, dag in dagbag.dags.items():
            print(dag_id,dag)
        self.assertEqual(len(dagbag.import_errors), 0,
                         'DAG import failures. Errors: {}'.format(dagbag.import_errors)
                         )

    def test_maintainer_email_present(self):
        dagbag = DagBag(dag_folder='../dags/',include_examples=False)
        for dag_id, dag in dagbag.dags.items():
            print(dag_id,dag)
            emails = dag.params.get('maintainer_email', [])
            msg = 'Maintainer email not set for DAG {id}'.format(id=dag_id)
            self.assertTrue(len(emails) >= 1, msg)
