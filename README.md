# togax-xml-layout-plugin

XML unofficial Toga layout parser


### Installation

[PyPi](https://pypi.org/project/togax-xml-layout-plugin/)

```
pip install togax-xml-layout-plugin
```

### Reason

Give developers the ability to define layouts in XML outside code. Also giving the final users the possibility to customize app layout without changing code.

### Example

layout.xml

```xml
<MainWindow>
	<SplitContainer>
		<ScrollContainer>
			<Box style="direction: column; padding: 10;">
				<!-- OptionContainer -->
				<OptionContainer id="container">
					<OptionItem text="1">
						<Box style="direction: column; padding: 10;">
							<!-- ImageView -->
							<Label>ImageView</Label>
							<ImageView>
								<Image src="resources/srtranslator.png" />
							</ImageView>

							<!-- WebView -->
							<Label>WebView</Label>
							<WebView url="https://beeware.org" style=" height: 500;" />

							<!-- Canvas -->
							<Label>Canvas</Label>
							<Canvas style="height: 100;" />

						</Box>
					</OptionItem>
					<OptionItem text="2">
						<Box style="direction: column; padding: 10;">
							<!-- DetailedList -->
							<Label>DetailedList</Label>
							<DetailedList>
								<accessors>
									<item>title</item>
									<item>subtitle</item>
									<item>icon</item>
								</accessors>
								<data>
									<item>
										<title>HEY 1</title>
										<subtitle>Selection Item 1</subtitle>
									</item>
									<item>
										<title>HEY 2</title>
										<subtitle>Selection Item 2</subtitle>
									</item>
									<item>
										<title>HEY 3</title>
										<subtitle>Selection Item 3</subtitle>
									</item>
								</data>
							</DetailedList>

							<!-- Table -->
							<Label>Table</Label>
							<Table>
								<headings>
									<item>name</item>
									<item>Age</item>
								</headings>
								<data>
									<item>
										<name>HEY 1</name>
										<age>Selection Item 1</age>
									</item>
									<item>
										<name>HEY 2</name>
										<age>Selection Item 2</age>
									</item>
									<item>
										<name>HEY 3</name>
										<age>Selection Item 3</age>
									</item>
								</data>
							</Table>
						</Box>
					</OptionItem>
				</OptionContainer>
			</Box>
		</ScrollContainer>
		<ScrollContainer>
			<Box style="direction: column; padding: 10;">
				<!-- ActivityIndicator -->
				<Label>ActivityIndicator</Label>
				<ActivityIndicator running="true" />

				<!-- ProgressBar -->
				<Label>ProgressBar</Label>
				<ProgressBar value="10" max="30" />

				<!-- Divider -->
				<Label>Divider</Label>
				<Divider />

				<!-- MultilineTextInput -->
				<Label>MultilineTextInput</Label>
				<MultilineTextInput
					value="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." />

				<!-- TextInput -->
				<Label>TextInput</Label>
				<TextInput value="Lorem ipsum dolor sit amet" />

				<!-- NumberInput -->
				<Label>NumberInput</Label>
				<NumberInput value="1000" />

				<!-- PasswordInput -->
				<Label>PasswordInput</Label>
				<PasswordInput />

				<!-- Button -->
				<Label>Button</Label>
				<Button on_press=".test_button">Button</Button>

				<!-- Slider -->
				<Label>Slider</Label>
				<Slider value="50" min="0" max="100" />

				<!-- Switch -->
				<Switch value="true">Switch</Switch>

				<!-- Selection -->
				<Label>Selection</Label>
				<Selection>
					<items>
						<item>Selection Item 1</item>
						<item>Selection Item 2</item>
						<item>Selection Item 3</item>
					</items>
				</Selection>

				<!-- Selection with dictionaries -->
				<Label>Selection with dictionaries</Label>
				<Selection>
					<items>
						<item>
							<name>HEY 1</name>
							<value>Selection Item 1</value>
						</item>
						<item>
							<name>HEY 2</name>
							<value>Selection Item 2</value>
						</item>
						<item>
							<name>HEY 3</name>
							<value>Selection Item 3</value>
						</item>
					</items>
				</Selection>
			</Box>
		</ScrollContainer>
	</SplitContainer>
</MainWindow>
```

app.py

```python
import toga
from togax_xml_layout import parse_layout

class App(toga.App):
    def startup(self):
        with open(f"{self.paths.app}/resources/layout.xml", "r") as f:
            self.main_window = parse_layout(self, f.read())
            self.main_window.show()
    def test_button(self, widget):
        print("clicked")
```
