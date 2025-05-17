import axios from 'axios';

// Use your computer's local IP and Flask port (5000)
const API_URL = 'http://10.37.123.125:5000';

// Create a new queue
export const createQueue = async (queue: {
  name: string,
  description?: string,
  location?: string,
  timePerPerson?: number
}) => {
  const res = await axios.post(`${API_URL}/queues`, queue);
  return res.data;
};

// Join a queue
export const joinQueue = async (queue_id: number, user: { name: string }) => {
  const res = await axios.post(`${API_URL}/queues/${queue_id}/join`, user);
  return res.data;
};

// Get all queues
export const getQueues = async () => {
  const res = await axios.get(`${API_URL}/queues`);
  return res.data;
};

// Get members of a queue
export const getQueueMembers = async (queue_id: number) => {
  const res = await axios.get(`${API_URL}/queues/${queue_id}/members`);
  return res.data;
};