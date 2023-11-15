namespace Calculadora
{
    partial class Calculadora
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            btnAdicao = new Button();
            btnSubtracao = new Button();
            btnMultiplicacao = new Button();
            btnDivisao = new Button();
            btnUm = new Button();
            btnDois = new Button();
            btnTres = new Button();
            btnSeis = new Button();
            btnCinco = new Button();
            btnQuatro = new Button();
            btnSete = new Button();
            btnOito = new Button();
            btnNove = new Button();
            btnZero = new Button();
            btnIgual = new Button();
            btnVirgula = new Button();
            btnLimpar = new Button();
            lblResultado = new Label();
            txtResultado = new TextBox();
            SuspendLayout();
            // 
            // btnAdicao
            // 
            btnAdicao.Location = new Point(214, 267);
            btnAdicao.Name = "btnAdicao";
            btnAdicao.Size = new Size(62, 57);
            btnAdicao.TabIndex = 13;
            btnAdicao.Text = "+";
            btnAdicao.UseVisualStyleBackColor = true;
            btnAdicao.Click += btnAdicao_Click;
            // 
            // btnSubtracao
            // 
            btnSubtracao.Location = new Point(214, 204);
            btnSubtracao.Name = "btnSubtracao";
            btnSubtracao.Size = new Size(62, 57);
            btnSubtracao.TabIndex = 14;
            btnSubtracao.Text = "-";
            btnSubtracao.UseVisualStyleBackColor = true;
            btnSubtracao.Click += btnSubtracao_Click;
            // 
            // btnMultiplicacao
            // 
            btnMultiplicacao.Location = new Point(214, 141);
            btnMultiplicacao.Name = "btnMultiplicacao";
            btnMultiplicacao.Size = new Size(62, 57);
            btnMultiplicacao.TabIndex = 15;
            btnMultiplicacao.Text = " x";
            btnMultiplicacao.UseVisualStyleBackColor = true;
            btnMultiplicacao.Click += btnMultiplicacao_Click;
            // 
            // btnDivisao
            // 
            btnDivisao.Location = new Point(214, 78);
            btnDivisao.Name = "btnDivisao";
            btnDivisao.Size = new Size(62, 57);
            btnDivisao.TabIndex = 16;
            btnDivisao.Text = " ÷";
            btnDivisao.UseVisualStyleBackColor = true;
            btnDivisao.Click += btnDivisao_Click;
            // 
            // btnUm
            // 
            btnUm.Location = new Point(10, 204);
            btnUm.Name = "btnUm";
            btnUm.Size = new Size(62, 57);
            btnUm.TabIndex = 1;
            btnUm.Text = "1\r\n";
            btnUm.UseVisualStyleBackColor = true;
            btnUm.Click += btnUm_Click;
            // 
            // btnDois
            // 
            btnDois.Location = new Point(78, 204);
            btnDois.Name = "btnDois";
            btnDois.Size = new Size(62, 57);
            btnDois.TabIndex = 2;
            btnDois.Text = "2";
            btnDois.UseVisualStyleBackColor = true;
            btnDois.Click += btnDois_Click;
            // 
            // btnTres
            // 
            btnTres.Location = new Point(146, 204);
            btnTres.Name = "btnTres";
            btnTres.Size = new Size(62, 57);
            btnTres.TabIndex = 3;
            btnTres.Text = "3";
            btnTres.UseVisualStyleBackColor = true;
            btnTres.Click += btnTres_Click;
            // 
            // btnSeis
            // 
            btnSeis.Location = new Point(146, 141);
            btnSeis.Name = "btnSeis";
            btnSeis.Size = new Size(62, 57);
            btnSeis.TabIndex = 4;
            btnSeis.Text = "6";
            btnSeis.UseVisualStyleBackColor = true;
            btnSeis.Click += btnSeis_Click;
            // 
            // btnCinco
            // 
            btnCinco.Location = new Point(78, 141);
            btnCinco.Name = "btnCinco";
            btnCinco.Size = new Size(62, 57);
            btnCinco.TabIndex = 5;
            btnCinco.Text = "5";
            btnCinco.UseVisualStyleBackColor = true;
            btnCinco.Click += btnCinco_Click;
            // 
            // btnQuatro
            // 
            btnQuatro.Location = new Point(10, 141);
            btnQuatro.Name = "btnQuatro";
            btnQuatro.Size = new Size(62, 57);
            btnQuatro.TabIndex = 6;
            btnQuatro.Text = "4";
            btnQuatro.UseVisualStyleBackColor = true;
            btnQuatro.Click += btnQuatro_Click;
            // 
            // btnSete
            // 
            btnSete.Location = new Point(10, 78);
            btnSete.Name = "btnSete";
            btnSete.Size = new Size(62, 57);
            btnSete.TabIndex = 7;
            btnSete.Text = "7";
            btnSete.UseVisualStyleBackColor = true;
            btnSete.Click += btnSete_Click;
            // 
            // btnOito
            // 
            btnOito.Location = new Point(78, 78);
            btnOito.Name = "btnOito";
            btnOito.Size = new Size(62, 57);
            btnOito.TabIndex = 8;
            btnOito.Text = "8";
            btnOito.UseVisualStyleBackColor = true;
            btnOito.Click += btnOito_Click;
            // 
            // btnNove
            // 
            btnNove.Location = new Point(146, 78);
            btnNove.Name = "btnNove";
            btnNove.Size = new Size(62, 57);
            btnNove.TabIndex = 9;
            btnNove.Text = "9";
            btnNove.UseVisualStyleBackColor = true;
            btnNove.Click += btnNove_Click;
            // 
            // btnZero
            // 
            btnZero.Location = new Point(78, 267);
            btnZero.Name = "btnZero";
            btnZero.Size = new Size(62, 57);
            btnZero.TabIndex = 10;
            btnZero.Text = "0";
            btnZero.UseVisualStyleBackColor = true;
            btnZero.Click += btn0_Click;
            // 
            // btnIgual
            // 
            btnIgual.Location = new Point(146, 267);
            btnIgual.Name = "btnIgual";
            btnIgual.Size = new Size(62, 57);
            btnIgual.TabIndex = 11;
            btnIgual.Text = "=";
            btnIgual.UseVisualStyleBackColor = true;
            btnIgual.Click += btnIgual_Click;
            // 
            // btnVirgula
            // 
            btnVirgula.Location = new Point(10, 267);
            btnVirgula.Name = "btnVirgula";
            btnVirgula.Size = new Size(62, 57);
            btnVirgula.TabIndex = 12;
            btnVirgula.Text = ",";
            btnVirgula.UseVisualStyleBackColor = true;
            btnVirgula.Click += btnVirgula_Click;
            // 
            // btnLimpar
            // 
            btnLimpar.Location = new Point(214, 48);
            btnLimpar.Name = "btnLimpar";
            btnLimpar.Size = new Size(62, 24);
            btnLimpar.TabIndex = 17;
            btnLimpar.Text = " C";
            btnLimpar.UseVisualStyleBackColor = true;
            btnLimpar.Click += btnLimpar_Click;
            // 
            // lblResultado
            // 
            lblResultado.AutoSize = true;
            lblResultado.BackColor = SystemColors.ButtonHighlight;
            lblResultado.Location = new Point(23, 18);
            lblResultado.Name = "lblResultado";
            lblResultado.Size = new Size(0, 15);
            lblResultado.TabIndex = 18;
            // 
            // txtResultado
            // 
            txtResultado.BackColor = SystemColors.ButtonHighlight;
            txtResultado.Location = new Point(10, 15);
            txtResultado.Name = "txtResultado";
            txtResultado.ReadOnly = true;
            txtResultado.Size = new Size(266, 23);
            txtResultado.TabIndex = 0;
            txtResultado.TextAlign = HorizontalAlignment.Right;
            // 
            // Calculadora
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(288, 336);
            Controls.Add(lblResultado);
            Controls.Add(btnLimpar);
            Controls.Add(btnDivisao);
            Controls.Add(btnMultiplicacao);
            Controls.Add(btnSubtracao);
            Controls.Add(btnAdicao);
            Controls.Add(btnVirgula);
            Controls.Add(btnIgual);
            Controls.Add(btnZero);
            Controls.Add(btnNove);
            Controls.Add(btnOito);
            Controls.Add(btnSete);
            Controls.Add(btnQuatro);
            Controls.Add(btnCinco);
            Controls.Add(btnSeis);
            Controls.Add(btnTres);
            Controls.Add(btnDois);
            Controls.Add(btnUm);
            Controls.Add(txtResultado);
            Name = "Calculadora";
            StartPosition = FormStartPosition.CenterScreen;
            Text = "Calculadora";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion
        private Button btnAdicao;
        private Button btnSubtracao;
        private Button btnMultiplicacao;
        private Button btnDivisao;
        private Button btnUm;
        private Button btnDois;
        private Button btnTres;
        private Button btnSeis;
        private Button btnCinco;
        private Button btnQuatro;
        private Button btnSete;
        private Button btnOito;
        private Button btnNove;
        private Button btnZero;
        private Button btnIgual;
        private Button btnVirgula;
        private Button btnLimpar;
        private Label lblResultado;
        private TextBox txtResultado;
    }
}