/*
 * =====================================================================================
 *
 *       Filename:  banco.c
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  17/06/2017 16:00:00
 *       Revision:  none
 *       Compiler:  gcc (GCC) 5.3.0
 *
 *         Authors: 
 *
 * =====================================================================================
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <locale.h>
#include <time.h>
#include "sqlite3.h" // SQLite header

typedef int bool;
#define TRUE  1
#define FALSE 0

bool isOpenDB = FALSE;

#define DB "banco.s3db"
// sqlite database pointer 
sqlite3 *dbfile;

/*---------------------------------------------------------------------------------*/

bool ConnectDB() //função para conexão com o banco de dados
{
   if (sqlite3_open(DB, &dbfile)==SQLITE_OK)
   {
      isOpenDB = TRUE;
      printf("Banco de dados aberto com sucesso!\n");
      system("pause");
      return TRUE;
   }         
   fprintf(stderr, "ERRO! Nao foi possivel abrir o banco de dados: %s\n", sqlite3_errmsg(dbfile));
   system("pause");
   return FALSE;
}

void DisconnectDB() //função para desconectar o acesso ao banco de dados
{
   if (isOpenDB == TRUE) 
   {
      printf("\nEncerrando conexao com o banco...\n\n");
      system("pause");
      sqlite3_close(dbfile);
   }
}

static int callback(void *NotUsed, int argc, char **argv, char **azColName){
   int i;
   for(i=0; i<argc; i++){
      printf("%s = %s\n", azColName[i], argv[i] ? argv[i] : "NULL");
   }
   printf("\n");
   return 0;
}

void cria_tabela_clientes() {
   int  rc;              // return code
   char *sql;            // pointer to an error string
   char *zErrMsg = 0;

   /* Cria query SQL */
   sql = "CREATE TABLE CLIENTES("  \
         "CONTA INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL," \
         "NOME CHAR(30) NOT NULL," \
         "SENHA INTEGER NOT NULL," \
         "SALDO DOUBLE NOT NULL," \
         "TRANSACAO CHAR(15) NOT NULL," \
         "VALOR DOUBLE NOT NULL," \
         "DATA CHAR(25) NOT NULL);";

   /* Executa query SQL */
   rc = sqlite3_exec(dbfile, sql, callback, 0, &zErrMsg);
   if(rc != SQLITE_OK){
      fprintf(stderr, "\nErro SQL: %s\n", zErrMsg);
      sqlite3_free(zErrMsg);
      system("pause");
   }

   else{
      fprintf(stdout, "\nTabela criada com sucesso!\n");
      system("pause");
   }
}

bool login_admin() {
   int senha,tentativas=3;
   system("cls");
   for(tentativas=3;tentativas>=0;tentativas--) {
      printf("\n\t\t\tBem vindo ao SisAut\n\n");
      printf("Insira sua senha de administrador:\n");
      scanf("%d",&senha);
      if(senha==123321){
         printf("\nBem vindo!\n\n");
         return TRUE;
      } else {
         printf("\nVoce ainta tem %d tentativas.\n",tentativas);
         system("pause");
         system("cls");
      }
   }
   return FALSE;
}

void incluir_cliente() {
   sqlite3_stmt *stmt;
   int rc;

   char nome[30];
   int conta, senha;
   double saldo;
   char transacao[15] = "Deposito";

   system("cls");
   printf ("\n******* Cadastro de Cliente *******\n");

   printf("\nInsira o nome do cliente: ");
   scanf("%s",&nome);
   fflush(stdin);

   printf("\nInsira uma senha numerica com 6 digitos: ");
   scanf("%d",&senha);
   fflush(stdin);

   printf("\nInsira um saldo inicial para o cliente: ");
   scanf("%lf",&saldo);
   fflush(stdin);

   time_t t = time(NULL);
   struct tm *tm = localtime(&t);

   sqlite3_prepare_v2(dbfile, "INSERT INTO CLIENTES (NOME, SENHA, SALDO, TRANSACAO, VALOR, DATA) values (?1, ?2, ?3, ?4, ?5, ?6);", -1, &stmt, NULL);
   sqlite3_bind_text(stmt, 1, nome, -1, SQLITE_STATIC);
   //sqlite3_bind_int(stmt, 2, conta);
   sqlite3_bind_int(stmt, 2, senha);
   sqlite3_bind_double(stmt, 3, saldo);
   sqlite3_bind_text(stmt, 4, transacao, -1, SQLITE_STATIC);
   sqlite3_bind_double(stmt, 5, saldo);
   sqlite3_bind_text(stmt, 6, asctime(tm), -1, SQLITE_STATIC);

   rc = sqlite3_step(stmt);
   if(rc != SQLITE_DONE) {
      printf("ERROR: %s\n", sqlite3_errmsg(dbfile));
   }

   sqlite3_finalize(stmt);
   free(stmt);
}

void listar_clientes() {
   char *zErrMsg = 0;
   int rc;
   const char* data = "Callback function called";
   char *sql = "SELECT * FROM CLIENTES";

   system("cls");
   printf("\n******* Listagem de Clientes *******\n");

   rc = sqlite3_exec(dbfile, sql, callback, (void*)data, &zErrMsg);
   if(rc != SQLITE_OK){
      fprintf(stderr, "SQL error: %s\n", zErrMsg);
      sqlite3_free(zErrMsg);
   }else{
      fprintf(stdout, "Operacao efetuada com sucesso!\n\n");
   }
}

void consultar_saldo() {
   sqlite3_stmt *stmt;
   int conta, senha;

   system("cls");
   printf("\n******* Consulta Saldo *******\n");

   printf("\nInsira o numero da conta: ");
   scanf("%d",&conta);
   fflush(stdin);

   printf("\nInsira a senha: ");
   scanf("%d",&senha);
   fflush(stdin);

   int rc = sqlite3_prepare_v2(dbfile, "SELECT SENHA,CONTA,NOME,SALDO FROM CLIENTES WHERE CONTA=?", -1, &stmt, NULL);
   sqlite3_bind_int(stmt, 1, conta);

   if (rc != SQLITE_OK) {
      printf("ERROR: %s\n\n", sqlite3_errmsg(dbfile));
   }

   else {
      rc = sqlite3_step(stmt);
      if (rc != SQLITE_DONE && rc != SQLITE_ROW) {
         printf("ERROR: %s\n\n", sqlite3_errmsg(dbfile));
      }

      else {
         if (rc == SQLITE_DONE) {
            printf("%s", "\nNenhum registro encontrado.\n\n");
         }

         else if (sqlite3_column_type(stmt, 0) == SQLITE_NULL) {
            printf("%s", "\nResultado nulo (NULL).\n\n");
         } 

         else { // some valid result
            if(senha==sqlite3_column_int(stmt, 0)) {
               printf("\n");
               printf("Conta: %d\n", sqlite3_column_int(stmt, 1));
               printf("Nome: %s\n", sqlite3_column_text(stmt, 2));
               printf("Saldo: R$%.2lf\n", sqlite3_column_double(stmt, 3));
               printf("\n");
            }
            else fprintf(stderr, "%s", "\nSenha errada! Operacao cancelada.\n\n");
         }
      }
   }
   sqlite3_finalize(stmt);
   free(stmt);
}

void saque() {    
   sqlite3_stmt *stmt;
   int conta, senha;
   double valor, saldo, novo_saldo;

   system("cls");
   printf("\n******* Saque *******\n");

   printf("\nInsira o numero da conta: ");
   scanf("%d",&conta);
   fflush(stdin);

   printf("\nInsira a senha: ");
   scanf("%d",&senha);
   fflush(stdin);

   int rc = sqlite3_prepare_v2(dbfile, "SELECT SENHA,CONTA,NOME,SALDO FROM CLIENTES WHERE CONTA=?", -1, &stmt, NULL);
   sqlite3_bind_int(stmt, 1, conta);

   if (rc != SQLITE_OK) {
      printf("ERROR: %s\n", sqlite3_errmsg(dbfile));
   }

   else {
      rc = sqlite3_step(stmt);
      if (rc != SQLITE_DONE && rc != SQLITE_ROW) {
         printf("ERROR: %s\n", sqlite3_errmsg(dbfile));
      }

      else {
         if (rc == SQLITE_DONE) {
            printf("%s", "No result.\n");
         }

         else if (sqlite3_column_type(stmt, 0) == SQLITE_NULL) {
            printf("%s", "Result is NULL.\n");
         } 

         else { // some valid result
            if(senha==sqlite3_column_int(stmt, 0)) {

               saldo = sqlite3_column_double(stmt, 3);
               printf("\nSaldo disponivel: R$%.2lf\n", saldo);

               printf("\nDigite o valor desejado: ");
               scanf("%lf",&valor);
               fflush(stdin);

               if(saldo >= valor) {
                  novo_saldo = saldo - valor;
                  printf("\nNovo saldo: R$%.2lf", novo_saldo);

                  int rc = sqlite3_prepare_v2(dbfile, "UPDATE CLIENTES SET SALDO=? WHERE CONTA=?", -1, &stmt, NULL);
                  sqlite3_bind_double(stmt, 1, novo_saldo);
                  sqlite3_bind_int(stmt, 2, conta);

                  rc = sqlite3_step(stmt);
                  if(rc != SQLITE_DONE) {
                     printf("ERROR: %s\n", sqlite3_errmsg(dbfile));
                     goto end;
                  }

                  int rc2 = sqlite3_prepare_v2(dbfile, "UPDATE CLIENTES SET TRANSACAO=? WHERE CONTA=?", -1, &stmt, NULL);
                  char transacao[] = "Saque";
                  sqlite3_bind_text(stmt, 1, transacao, -1, SQLITE_STATIC);
                  sqlite3_bind_int(stmt, 2, conta);

                  rc2 = sqlite3_step(stmt);
                  if(rc2 != SQLITE_DONE) {
                     printf("ERROR: %s\n", sqlite3_errmsg(dbfile));
                     goto end;
                  }

                  int rc3 = sqlite3_prepare_v2(dbfile, "UPDATE CLIENTES SET VALOR=? WHERE CONTA=?", -1, &stmt, NULL);
                  sqlite3_bind_double(stmt, 1, valor);
                  sqlite3_bind_int(stmt, 2, conta);

                  rc3 = sqlite3_step(stmt);
                  if(rc3 != SQLITE_DONE) {
                     printf("ERROR: %s\n", sqlite3_errmsg(dbfile));
                     goto end;
                  }

                  time_t t = time(NULL);
                  struct tm *tm = localtime(&t);

                  int rc4 = sqlite3_prepare_v2(dbfile, "UPDATE CLIENTES SET DATA=? WHERE CONTA=?", -1, &stmt, NULL);
                  sqlite3_bind_text(stmt, 1, asctime(tm), -1, SQLITE_STATIC);
                  sqlite3_bind_int(stmt, 2, conta);

                  rc4 = sqlite3_step(stmt);
                  if(rc4 != SQLITE_DONE) {
                     printf("ERROR: %s\n", sqlite3_errmsg(dbfile));
                     goto end;
                  }

                  printf("%s","\nSaque realizado com sucesso!\n\n");
               }
               else fprintf(stderr, "%s", "\nSaldo insuficiente! Operacao cancelada.\n\n");
            }
            else fprintf(stderr, "%s", "\nSenha errada! Operacao cancelada.\n\n");
         }
      }
   }
   end:
      sqlite3_finalize(stmt);
      free(stmt);
}

void deposito() {    
   sqlite3_stmt *stmt;
   int conta, senha;
   double valor, saldo, novo_saldo;

   system("cls");
   printf("\n******* Deposito *******\n");

   printf("\nInsira o numero da conta: ");
   scanf("%d",&conta);
   fflush(stdin);

   printf("\nInsira a senha: ");
   scanf("%d",&senha);
   fflush(stdin);

   int rc = sqlite3_prepare_v2(dbfile, "SELECT SENHA,CONTA,NOME,SALDO FROM CLIENTES WHERE CONTA=?", -1, &stmt, NULL);
   sqlite3_bind_int(stmt, 1, conta);

   if (rc != SQLITE_OK) {
      printf("ERROR: %s\n", sqlite3_errmsg(dbfile));
   }

   else {
      rc = sqlite3_step(stmt);
      if (rc != SQLITE_DONE && rc != SQLITE_ROW) {
         printf("ERROR: %s\n", sqlite3_errmsg(dbfile));
      }

      else {
         if (rc == SQLITE_DONE) {
            printf("%s", "No result.\n");
         }

         else if (sqlite3_column_type(stmt, 0) == SQLITE_NULL) {
            printf("%s", "Result is NULL.\n");
         } 

         else { // some valid result
            if(senha==sqlite3_column_int(stmt, 0)) {

               saldo = sqlite3_column_double(stmt, 3);
               printf("\nSaldo disponivel: R$%.2lf\n", saldo);

               printf("\nDigite o valor do deposito: ");
               scanf("%lf",&valor);
               fflush(stdin);

               if(valor > 0) {
                  novo_saldo = saldo + valor;
                  printf("\nNovo saldo: R$%.2lf", novo_saldo);

                  int rc = sqlite3_prepare_v2(dbfile, "UPDATE CLIENTES SET SALDO=? WHERE CONTA=?", -1, &stmt, NULL);
                  sqlite3_bind_double(stmt, 1, novo_saldo);
                  sqlite3_bind_int(stmt, 2, conta);

                  rc = sqlite3_step(stmt);
                  if(rc != SQLITE_DONE) {
                     printf("ERROR: %s\n", sqlite3_errmsg(dbfile));
                     goto end;
                  }

                  int rc2 = sqlite3_prepare_v2(dbfile, "UPDATE CLIENTES SET TRANSACAO=? WHERE CONTA=?", -1, &stmt, NULL);
                  char transacao[] = "Deposito";
                  sqlite3_bind_text(stmt, 1, transacao, -1, SQLITE_STATIC);
                  sqlite3_bind_int(stmt, 2, conta);

                  rc2 = sqlite3_step(stmt);
                  if(rc2 != SQLITE_DONE) {
                     printf("ERROR: %s\n", sqlite3_errmsg(dbfile));
                     goto end;
                  }

                  int rc3 = sqlite3_prepare_v2(dbfile, "UPDATE CLIENTES SET VALOR=? WHERE CONTA=?", -1, &stmt, NULL);
                  sqlite3_bind_double(stmt, 1, valor);
                  sqlite3_bind_int(stmt, 2, conta);

                  rc3 = sqlite3_step(stmt);
                  if(rc3 != SQLITE_DONE) {
                     printf("ERROR: %s\n", sqlite3_errmsg(dbfile));
                     goto end;
                  }

                  time_t t = time(NULL);
                  struct tm *tm = localtime(&t);

                  int rc4 = sqlite3_prepare_v2(dbfile, "UPDATE CLIENTES SET DATA=? WHERE CONTA=?", -1, &stmt, NULL);
                  sqlite3_bind_text(stmt, 1, asctime(tm), -1, SQLITE_STATIC);
                  sqlite3_bind_int(stmt, 2, conta);

                  rc4 = sqlite3_step(stmt);
                  if(rc4 != SQLITE_DONE) {
                     printf("ERROR: %s\n", sqlite3_errmsg(dbfile));
                     goto end;
                  }

                  printf("%s","\nDeposito realizado com sucesso!\n\n");
               }
               else fprintf(stderr, "%s", "\nValor invalido! Operacao cancelada.\n\n");
            }
            else fprintf(stderr, "%s", "\nSenha errada! Operacao cancelada.\n\n");
         }
      }
   }
   end:
      sqlite3_finalize(stmt);
      free(stmt);
}

void extrato() {
   sqlite3_stmt *stmt;
   int conta, senha;
   double valor, saldo, novo_saldo;

   system("cls");
   printf("\n******* Extrato *******\n");

   printf("\nInsira o numero da conta: ");
   scanf("%d",&conta);
   fflush(stdin);

   printf("\nInsira a senha: ");
   scanf("%d",&senha);
   fflush(stdin);

   int rc = sqlite3_prepare_v2(dbfile, "SELECT CONTA,NOME,SENHA,TRANSACAO,VALOR,DATA FROM CLIENTES WHERE CONTA=?", -1, &stmt, NULL);
   sqlite3_bind_int(stmt, 1, conta);

   if (rc != SQLITE_OK) {
      printf("ERROR: %s\n\n", sqlite3_errmsg(dbfile));
   }

   else {
      rc = sqlite3_step(stmt);
      if (rc != SQLITE_DONE && rc != SQLITE_ROW) {
         printf("ERROR: %s\n\n", sqlite3_errmsg(dbfile));
      }

      else {
         if (rc == SQLITE_DONE) {
            printf("%s", "\nNenhum registro encontrado.\n\n");
         }

         else if (sqlite3_column_type(stmt, 0) == SQLITE_NULL) {
            printf("%s", "\nResultado nulo (NULL).\n\n");
         } 

         else { // some valid result
            if(senha==sqlite3_column_int(stmt, 2)) {
               system("cls");
               printf("\n******* Extrato *******\n");
               printf("\nConta: %d", sqlite3_column_int(stmt, 0));
               printf("\nNome: %s", sqlite3_column_text(stmt, 1));
               printf("\nUltima transacao: %s", sqlite3_column_text(stmt, 3));
               printf("\nValor: R$%.2lf", sqlite3_column_double(stmt, 4));
               printf("\nData: %s\n", sqlite3_column_text(stmt, 5));
            }
            else fprintf(stderr, "%s", "\nSenha errada! Operacao cancelada.\n\n");
         }
      }
   }
   sqlite3_finalize(stmt);
   free(stmt);
}

int menu(){
   int opc;
   system("cls");
   system("color 3F");
   printf("\t\t\tSisAut CAIXA\n");
   printf("\n---------------------------------------------------\n");
   printf("\n\n\t\t\t MENU\n\n");
   printf(" 1 - Cadastrar Novo Cliente\n 2 - Listar Clientes\n 3 - Consultar Saldo do Cliente\n 4 - Saque\n 5 - Deposito\n 6 - Extrato\n 7 - Sair\n");
   printf("\nEscolha uma opcao: ");
   fflush(stdin);
   scanf("%i",&opc);
   switch(opc)
   {
      case 1: incluir_cliente(); menu(); break;

      case 2: listar_clientes(); system("pause"); menu(); break;

      case 3: consultar_saldo(); system("pause"); menu(); break;

      case 4: saque(); system("pause"); menu(); break;

      case 5: deposito(); system("pause"); menu(); break;

      case 6: extrato(); system("pause"); menu(); break;
      
      case 7: printf("\nSaindo do sistema...\n"); break;

      default: printf("\nOpcao invalida!\n\n"); system("pause"); menu(); break;
   }
}

int main() {
   system("title BANCO");
   system("color 1F");
   setlocale(LC_ALL, "Portuguese");

   int opcao = login_admin();
   if(opcao=TRUE) {
      ConnectDB();
      cria_tabela_clientes();
      menu();
      DisconnectDB();
   }

   return 0;
}