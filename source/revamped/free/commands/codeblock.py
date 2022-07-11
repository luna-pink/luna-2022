from discord.ext import commands


class CodeblockCog(commands.Cog, name="Codeblock commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="codeblock_css",
        usage="<text>",
        description="CSS codeblock"
    )
    async def codeblock_css(self, luna, *, text: str):
        await luna.send(f"```css\n{text}\n```")

    @commands.command(
        name="codeblock_brainfuck",
        usage="<text>",
        description="Brainfuck codeblock"
    )
    async def codeblock_brainfuck(self, luna, *, text: str):
        await luna.send(f"```brainfuck\n{text}\n```")

    @commands.command(
        name="codeblock_md",
        usage="<text>",
        description="MD codeblock"
    )
    async def codeblock_md(self, luna, *, text: str):
        await luna.send(f"```md\n{text}\n```")

    @commands.command(
        name="codeblock_fix",
        usage="<text>",
        description="Fix codeblock"
    )
    async def codeblock_fix(self, luna, *, text: str):
        await luna.send(f"```fix\n{text}\n```")

    @commands.command(
        name="codeblock_glsl",
        usage="<text>",
        description="Glsl codeblock"
    )
    async def codeblock_glsl(self, luna, *, text: str):
        await luna.send(f"```glsl\n{text}\n```")

    @commands.command(
        name="codeblock_diff",
        usage="<text>",
        description="Diff codeblock"
    )
    async def codeblock_diff(self, luna, *, text: str):
        await luna.send(f"```diff\n{text}\n```")

    @commands.command(
        name="codeblock_bash",
        usage="<text>",
        description="Bash codeblock"
    )
    async def codeblock_bash(self, luna, *, text: str):
        await luna.send(f"```bash\n{text}\n```")

    @commands.command(
        name="codeblock_cs",
        usage="<text>",
        description="C# codeblock"
    )
    async def codeblock_cs(self, luna, *, text: str):
        await luna.send(f"```cs\n{text}\n```")

    @commands.command(
        name="codeblock_cpp",
        usage="<text>",
        description="C++ codeblock"
    )
    async def codeblock_cpp(self, luna, *, text: str):
        await luna.send(f"```cpp\n{text}\n```")

    @commands.command(
        name="codeblock_ini",
        usage="<text>",
        description="Ini codeblock"
    )
    async def codeblock_ini(self, luna, *, text: str):
        await luna.send(f"```ini\n{text}\n```")

    @commands.command(
        name="codeblock_asciidoc",
        usage="<text>",
        description="Asciidoc codeblock"
    )
    async def codeblock_asciidoc(self, luna, *, text: str):
        await luna.send(f"```asciidoc\n{text}\n```")

    @commands.command(
        name="codeblock_autohotkey",
        usage="<text>",
        description="Autohotkey codeblock"
    )
    async def codeblock_autohotkey(self, luna, *, text: str):
        await luna.send(f"```autohotkey\n{text}\n```")

    @commands.command(
        name="codeblock_python",
        usage="<text>",
        description="Python codeblock"
    )
    async def codeblock_python(self, luna, *, text: str):
        await luna.send(f"```python\n{text}\n```")

    @commands.command(
        name="codeblock_lua",
        usage="<text>",
        description="Lua codeblock"
    )
    async def codeblock_lua(self, luna, *, text: str):
        await luna.send(f"```lua\n{text}\n```")

    @commands.command(
        name="codeblock_php",
        usage="<text>",
        description="PHP codeblock"
    )
    async def codeblock_php(self, luna, *, text: str):
        await luna.send(f"```php\n{text}\n```")

    @commands.command(
        name="codeblock_rust",
        usage="<text>",
        description="Rust codeblock"
    )
    async def codeblock_rust(self, luna, *, text: str):
        await luna.send(f"```rust\n{text}\n```")

    @commands.command(
        name="codeblock_java",
        usage="<text>",
        description="Java codeblock"
    )
    async def codeblock_java(self, luna, *, text: str):
        await luna.send(f"```java\n{text}\n```")

    @commands.command(
        name="codeblock_kotlin",
        usage="<text>",
        description="Kotlin codeblock"
    )
    async def codeblock_kotlin(self, luna, *, text: str):
        await luna.send(f"```kotlin\n{text}\n```")

    @commands.command(
        name="codeblock_js",
        usage="<text>",
        description="Javascript codeblock"
    )
    async def codeblock_js(self, luna, *, text: str):
        await luna.send(f"```javascript\n{text}\n```")

    @commands.command(
        name="codeblock_mysql",
        usage="<text>",
        description="MySQL codeblock"
    )
    async def codeblock_mysql(self, luna, *, text: str):
        await luna.send(f"```MySQL\n{text}\n```")

    @commands.command(
        name="codeblock_mk",
        usage="<text>",
        description="Markdown codeblock"
    )
    async def codeblock_mk(self, luna, *, text: str):
        await luna.send(f"```markdown\n{text}\n```")

    @commands.command(
        name="codeblock_ansi",
        usage="<text>",
        description="Ansi codeblock"
    )
    async def codeblock_ansi(self, luna, *, text: str):
        await luna.send(f"```ansi\n{text}\n```")