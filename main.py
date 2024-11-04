import matplotlib.pyplot as plt
import dotenv, os, traceback, discord
from discord import app_commands
from io import BytesIO


client = discord.Client(intents = discord.Intents.all())
tree = app_commands.CommandTree(client)

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)
TOKEN = os.environ.get("TOKEN")

HELP_MESSAGE="""
## <:latexer_0:1302653771645714555><:latexer_1:1302653792239484928><:latexer_2:1302653813156610118>ヘルプ
`/compile_latex`
LaTeXをコンパイルします。
LaTeXの書式については[こちら](https://www.cmor-faculty.rice.edu/~heinken/latex/symbols.pdf)を参照してください。
引数:
- `latex_code` LaTeXのコードを入力します。
- `font_size` フォントサイズを入力します。既定値は10です。
- `silent` Trueを指定すると自分にのみ見えるメッセージとして送信されます。既定値はFalseです。
- `font_type` フォントの種類を入力します。既定値はcmです。

-# Copyright 2024 niwatori-chicken
-# Github: <https://github.com/niwatori-chicken/latexer-discord-bot>
"""

@client.event
async def on_ready():
        print("now ready")

@client.event
async def setup_hook() -> None:
        await tree.sync()

@tree.command(name="compile_latex", description="LaTeXをコンパイルします。詳しくは/helpコマンドを実行してください。")
async def compile_latex(interaction:discord.Interaction, latex_code:str, font_size:int=10, silent:bool=False, font_type:str="cm"):
    if silent:
            await interaction.response.defer(ephemeral=True)
    else:
            await interaction.response.defer(ephemeral=False)

    try:
        buffer = BytesIO()
        fig = plt.figure()

        fig.text(0.5, 0.5, f"${latex_code}$", ha='center', va='center', fontsize=font_size, math_fontfamily=font_type)
        fig.savefig(buffer, dpi=600, bbox_inches='tight', pad_inches=0.05, transparent=False)
        buffer.seek(0)
        
    except Exception:
          print(traceback.format_exc())
          await interaction.followup.send(content=f"エラーが発生しました。\n```{traceback.format_exc(limit=1)}```\n`/help`でヘルプを見ることができます。", ephemeral=True)
          plt.close(fig)
          return

    await interaction.followup.send(file=discord.File(buffer, filename="output.png"))
    plt.close(fig)

@tree.command(name="help", description="ヘルプを表示します。")
async def help(interaction:discord.Interaction):
      await interaction.response.send_message(content=HELP_MESSAGE, ephemeral=True)

client.run(TOKEN)
