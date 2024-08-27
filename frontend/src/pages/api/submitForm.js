import formidable from 'formidable';
import fs from "fs";
import FormData from 'form-data';
import axios from 'axios';

export const config = {
  api: {
    bodyParser: false,
  },
};

export default async function handler(req, res) {
  if (req.method === 'POST') {
    const form = formidable({});

    form.parse(req, async (err, fields, files) => {
      if (err) {
        res.status(500).json({ error: err });
        return;
      }

      const { model, library } = fields;

      const filepath = files.file[0].filepath;
      const filename = files.file[0].originalFilename;
      const fileBuffer = fs.readFileSync(filepath);

      const formData = new FormData();
      formData.append('file', fileBuffer, { filename: filename });
      formData.append('model_name', model[0]);
      formData.append('library_name', library[0]);

      const headers = {
        'x-api-key': process.env.API_KEY
      }

      try {
        const response = await axios.post(`${process.env.API_HOST}/predict`, formData, { headers: headers });

        res.status(response.status).json(response.data);
      } catch (error) {
        res.status(500).json({ error: error });
      }
    });
  } else {
    res.status(405).json({ error: 'Método no permitido' });
  }
}
