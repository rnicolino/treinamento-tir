from tir import Webapp
from datetime import date
import unittest

class TAFA232(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		data_Sistema = date.today()
		data = data_Sistema.strftime('%d/%m/%Y')
		inst.oHelper.Setup('SIGATAF',data,'T1','D MG 01')
		inst.oHelper.Program('TAFA232')	

	def test_TAFA232_CT001(self):

		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch("D MG 01 ")
		self.oHelper.SetValue("C8R_CODRUB","COD_RUB_TIR")
		self.oHelper.SetValue("C8R_DTINI","012020")
		self.oHelper.SetValue("C8R_IDTBRU","000003")
		self.oHelper.SetValue("C8R_DESRUB","TESTE RUBRICA TIR")
		self.oHelper.SetValue("C8R_NATRUB","000001")
		self.oHelper.SetValue("C8R_INDTRB","1")
		self.oHelper.SetValue("C8R_CINTPS","000001")
		self.oHelper.SetValue("C8R_CINTIR","000001")
		self.oHelper.SetValue("C8R_CINTFG","00")
		self.oHelper.SetValue("C8R_CINTSL","00")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()