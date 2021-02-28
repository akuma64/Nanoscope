/* SPDX-License-Identifier: GPL-3.0-only */

#define ICECK LED_BUILTIN
#define ICEDA  0x12

void step()
{
	digitalWrite(ICECK, HIGH);
	digitalWrite(ICECK, LOW);
}

int read_bit()
{
	return digitalRead(ICEDA);
}

/*
 * `setup' opens the initial serial connection to the Arduino, delegates ICEDA &
 * ICECK pin modes, and cycles ICECK 8x (byte) while reading ICEDA every step. 
 */
void setup()
{
	Serial.begin(9600);

	pinMode(ICECK, OUTPUT);
	pinMode(ICEDA, INPUT);

	/* Print any prematurely received data */
	if (Serial.available() > 0) {
		Serial.println(Serial.read(), HEX);
	}

	delay(2000);

	for (int i = 0; i < 8; i++)
	{
		step();
		Serial.println(read_bit());
	}

	Serial.flush();
}

void loop() {} /* Forgo the infinte loop and only execute once. */